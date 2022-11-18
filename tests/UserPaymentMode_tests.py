#!/usr/bin/python3
"""
    UserPaymentMode package tests
    2022-11-19 00:56
"""

import unittest
from context import UserPaymentMode


class Test(unittest.TestCase):

    def test_csv_string_empty(self):
        self.assertRaises(Exception, UserPaymentMode.UserPaymentMode, '')

    def test_csv_string_wrong_number_of_fields(self):
        self.assertRaises(Exception, UserPaymentMode.UserPaymentMode, 'token;', ';')

    def test_wrong_token(self):
        self.assertRaises(Exception, UserPaymentMode.UserPaymentMode, ';1', ';')

    def test_wrong_mode(self):
        self.assertRaises(Exception, UserPaymentMode.UserPaymentMode, 'token;20', ';')

    def test_category_object_created(self):
        try:
            UserPaymentMode.UserPaymentMode('Token;1', ";")
        except Exception:
            self.fail("test_category_object_created")

    def test_category_check_mememship(self):
        cat = UserPaymentMode.UserPaymentMode('Token;1', ";")
        self.assertTrue(cat.checkMembership('Token found'))
        self.assertTrue(cat.checkMembership('token not found'))
        self.assertFalse(cat.checkMembership('toke not found'))

    def test_toCSV(self):
        cat = UserPaymentMode.UserPaymentMode('Token;1')
        self.assertEqual('token;1', cat.toCSV())


if __name__ == "__main__":

    unittest.main()
