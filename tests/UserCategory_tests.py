#!/usr/bin/python3
"""
    HomeBankCategories package tests
    2022-09-01 23:07
"""

import unittest
from context import UserCategory


class Test(unittest.TestCase):

    def test_csv_string_empty(self):
        self.assertRaises(Exception, UserCategory.UserCategory, '')

    def test_csv_string_wrong_number_of_fields(self):
        self.assertRaises(Exception, UserCategory.UserCategory, 'token;Cat', ';')

    def test_wrong_token(self):
        self.assertRaises(Exception, UserCategory.UserCategory, ';-;Category', ';')

    def test_wrong_sign(self):
        self.assertRaises(Exception, UserCategory.UserCategory, 'token;t;Category', ';')

    def test_wrong_category_name(self):
        self.assertRaises(Exception, UserCategory.UserCategory, 'token;-;', ';')

    def test_category_object_created(self):
        try:
            UserCategory.UserCategory('Token;-;Category', ";")
            UserCategory.UserCategory('Token;+;Category', ";")
        except Exception:
            self.fail("test_category_object_created")

    def test_category_check_mememship(self):
        cat = UserCategory.UserCategory('Token;-;Category', ";")
        self.assertTrue(cat.checkMembership('Token found'))
        self.assertTrue(cat.checkMembership('token not found'))
        self.assertFalse(cat.checkMembership('toke not found'))

    def test_toCSV(self):
        cat = UserCategory.UserCategory('Token;-;Category')
        self.assertEqual('token;-;Category', cat.toCSV())


if __name__ == "__main__":

    unittest.main()
