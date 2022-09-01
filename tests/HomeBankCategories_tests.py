"""
    HomeBankCategories package tests
    2022-09-01 23:07
"""

import unittest
from context import HomeBankCategories


class TestHomeBankCategories(unittest.TestCase):

    def test_parse_category_list_unavailable_file(self):
        expense_categories = []
        income_categories = []
        self.assertTrue(HomeBankCategories.parse_category_list("unknown.xhb",
                                                               expense_categories,
                                                               income_categories))


if __name__ == "__main__":

    unittest.main()
