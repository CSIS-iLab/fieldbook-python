#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_fieldbook
----------------------------------

Tests for `fieldbook` module.
"""

import unittest
import os

from fieldbook import Fieldbook


class TestFieldbook(unittest.TestCase):

    def setUp(self):
        os.environ['FIELDBOOK_API_KEY'] = 'TEST_ENV_KEY'
        os.environ['FIELDBOOK_API_SECRET'] = 'TEST_ENV_SECRET'

    def tearDown(self):
        pass

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


if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
