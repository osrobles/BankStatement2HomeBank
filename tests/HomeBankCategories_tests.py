#!/usr/bin/python3
"""
    HomeBankCategories package tests
    2022-09-01 23:07
"""

import unittest
from context import HomeBankCategories


class Test(unittest.TestCase):

    def test_unavailable_file(self):
        hbcategories = HomeBankCategories.HomeBankCategories('unknown.xhb')
        self.assertEqual(hbcategories.status, True)

    def test_list_correct_file(self):
        hbcategories = HomeBankCategories.HomeBankCategories('data/test.xhb')
        self.assertEqual(hbcategories.status, False)
        self.assertGreater(len(hbcategories.income_categories), 0)
        self.assertGreater(len(hbcategories.expense_categories), 0)


if __name__ == "__main__":

    unittest.main()
