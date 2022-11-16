#!/usr/bin/python3
"""
    HomeBankCategories package tests
    2022-09-01 23:07
"""

import unittest
from context import UserCategory


class Test(unittest.TestCase):

    def test_wrong_token(self):
        self.assertRaises(Exception, UserCategory.UserCategory, '', 'Category name')

    def test_wrong_category_name(self):
        self.assertRaises(Exception, UserCategory.UserCategory, 'Token', '')

    def test_category_object_created(self):
        try:
            UserCategory.UserCategory('Token', 'Category name')
        except Exception:
            self.fail("test_category_object_created")

    def test_category_check_mememship(self):
        cat = UserCategory.UserCategory('Token', 'Category name')
        self.assertTrue(cat.checkMembership('Token found'))
        self.assertTrue(cat.checkMembership('token not found'))
        self.assertFalse(cat.checkMembership('toke not found'))


if __name__ == "__main__":

    unittest.main()
