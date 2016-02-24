#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_fieldbook
----------------------------------

Tests for `fieldbook` module.
"""

import unittest
from unittest.mock import MagicMock
import os

from fieldbook import Fieldbook


class TestFieldbook(unittest.TestCase):

    def setUp(self):
        os.environ['FIELDBOOK_API_KEY'] = 'TEST_ENV_KEY'
        os.environ['FIELDBOOK_API_SECRET'] = 'TEST_ENV_SECRET'

    def tearDown(self):
        pass

    def test_client_makes_correct_urls(self):
        expected_url = 'https://api.fieldbook.com/v1/fakebook/fakesheet'
        client = Fieldbook()

        url_val = client._make_url('fakebook', sheet_name='fakesheet')

        self.assertEqual(url_val, expected_url)

    def test_client_intialize_with_authentication(self):
        client = Fieldbook(key='foo', secret='bar')

        self.assertEqual(client._key, 'foo')
        self.assertEqual(client._secret, 'bar')
        self.assertEqual(client.session.auth, ('foo', 'bar'))

    def test_client_set_auth_separately(self):
        client = Fieldbook()
        client.set_auth('foo', 'bar')

        self.assertEqual(client._key, 'foo')
        self.assertEqual(client._secret, 'bar')
        self.assertEqual(client.session.auth, ('foo', 'bar'))

    def test_client_auth_from_env(self):
        client = Fieldbook()

        self.assertEqual(client._key, 'TEST_ENV_KEY')
        self.assertEqual(client._secret, 'TEST_ENV_SECRET')
        self.assertEqual(client.session.auth, ('TEST_ENV_KEY', 'TEST_ENV_SECRET'))

    def test_client_get_sheets(self):
        client = Fieldbook()
        expected_value = ["foo", "bar", "baz"]

        client._get = MagicMock(return_value=expected_value)
        value = client.sheets('fakebook')

        client._get.assert_called_with('fakebook')
        self.assertListEqual(value, expected_value)

    def test_client_get_sheets_using_initial_book_id(self):
        client = Fieldbook(book_id='fakebook')
        expected_value = ["foo", "bar", "baz"]

        client._get = MagicMock(return_value=expected_value)
        client.sheets()

        self.assertIsNotNone(client.book_id)
        client._get.assert_called_with('fakebook')

    def test_client_get_sheet(self):
        client = Fieldbook(book_id='fakebook')
        expected_value = [
            {
                "id": 12,
                "record_url": "https://fieldbook.com/records/fakesheet",
                "column1": "text",
                "column2": []
            }
        ]

        client._get = MagicMock(return_value=expected_value)

        value = client.get('fakesheet')

        self.assertIsNotNone(client.book_id)
        client._get.assert_called_with('fakebook', sheet_name='fakesheet', params=None)
        self.assertListEqual(value, expected_value)
        self.assertIn('column2', value[0])
        self.assertListEqual(value[0]['column2'], [])

    def test_sheet_query_params_passed(self):
        client = Fieldbook(book_id='fakebook')

        expected_value = [
            {
                "id": 12,
                "record_url": "https://fieldbook.com/records/fakesheet",
                "column1": "text",
                "column2": []
            }
        ]

        client._get = MagicMock(return_value=expected_value)
        value = client.get('fakesheet', params={'column1': 'text'})

        self.assertIsNotNone(client.book_id)
        client._get.assert_called_with('fakebook', sheet_name='fakesheet', params={'column1': 'text'})
        self.assertListEqual(value, expected_value)


if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
