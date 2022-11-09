#!/usr/bin/python3
"""
    HomeBankCategories package tests
    2022-09-01 23:07
"""

import unittest
from context import Category


class Test(unittest.TestCase):

    def test_wrong_token(self):
        self.assertRaises(Exception, Category.Category, '', 'Category name')

    def test_wrong_category_name(self):
        self.assertRaises(Exception, Category.Category, 'Token', '')

    def test_category_object_created(self):
        try:
            Category.Category('Token', 'Category name')
        except Exception:
            self.fail("test_category_object_created")

    def test_category_check_mememship(self):
        cat = Category.Category('Token', 'Category name')
        self.assertTrue(cat.checkMembership('Token found'))
        self.assertTrue(cat.checkMembership('token not found'))
        self.assertFalse(cat.checkMembership('toke not found'))


if __name__ == "__main__":

    unittest.main()
