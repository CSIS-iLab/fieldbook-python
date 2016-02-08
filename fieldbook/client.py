# -*- coding: utf-8 -*-

import requests
from urllib.parse import urljoin


class Fieldbook(object):
    """Client for Fieldbook API: https://github.com/fieldbook/api-docs"""
    BASE_URL = "https://api.fieldbook.com"
    API_VERSION = "v1"

    def __init__(self, key=None, secret=None, book_id=None):
        super(Fieldbook, self).__init__()
        self._key = key
        self._secret = secret
        self.book_id = book_id
        self.session = requests.Session()
        if self._key and self._secret:
            self.set_auth(self._key, self._secret)

    def set_auth(self, key, secret):
        self.session.auth = (key, secret)

    def _make_url(self, book_id, sheet_name=None):
        return urljoin(Fieldbook.BASE_URL, "/".join((Fieldbook.API_VERSION, book_id, sheet_name or '')))

    def _get(self, book_id=None, sheet_name=None, params=None):
        if not self.session.auth and self._key and self._secret:
            self.set_auth(self._key, self._secret)
        if not book_id and not self.book_id:
            msg = 'You must either set `book_id` on the Fieldbook object or pass it as an argument to the endpoint method.'
            raise Exception(msg)
        url = self._make_url(book_id or self.book_id, sheet_name=sheet_name)
        resp = self.session.get(url, params=params)
        if not resp.ok:
            raise resp.raise_for_status()
        return resp.json()

    def sheets(self, book_id=None):
        """Returns a list of sheets associated with a book"""
        return self._get(book_id)

    def get(self, sheet_name, book_id=None, params=None):
        """Query a named sheet"""
        return self._get(book_id, sheet_name=sheet_name, params=params)
