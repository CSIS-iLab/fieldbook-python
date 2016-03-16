# -*- coding: utf-8 -*-

import requests
from urllib.parse import urljoin
from os import getenv


class Fieldbook(object):
    """
        Client for Fieldbook API: https://github.com/fieldbook/api-docs
        Initialize with a fieldbook_id and optionally the api key (name) and secret.
    """
    BASE_URL = "https://api.fieldbook.com"
    API_VERSION = "v1"

    def __init__(self, book_id, key=None, secret=None):
        super(Fieldbook, self).__init__()
        self._key = key if key else getenv('FIELDBOOK_API_KEY', None)
        self._secret = secret if secret else getenv('FIELDBOOK_API_SECRET', None)
        self.book_id = book_id
        self.session = requests.Session()
        if self._key and self._secret:
            self.set_auth(self._key, self._secret)

    def set_auth(self, key, secret):
        self._key = key
        self._secret = secret
        self.session.auth = (self._key, self._secret)

    def _make_url(self, sheet_name=None):
        return urljoin(Fieldbook.BASE_URL, "/".join((Fieldbook.API_VERSION, self.book_id, sheet_name or '')))

    def _get(self, sheet_name=None, params=None):
        if not self.session.auth and self._key and self._secret:
            self.set_auth(self._key, self._secret)
        url = self._make_url(sheet_name=sheet_name)
        resp = self.session.get(url, params=params)
        if not resp.ok:
            raise resp.raise_for_status()
        return resp.json()

    def sheets(self):
        """Returns a list of sheets associated with a book"""
        return self._get()

    def get(self, sheet_name, params=None):
        """Query a named sheet"""
        return self._get(sheet_name=sheet_name, params=params)
