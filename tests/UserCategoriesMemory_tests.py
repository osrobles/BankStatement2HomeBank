#!/usr/bin/python3
"""
    UserCategoriesMemory module tests
    2022-11-16 22:49
"""

import unittest
import os
from shutil import copyfile
from context import HomeBankCategories as hbc
from context import UserCategory as uc
from context import UserCategoriesMemory as ucm


class Test(unittest.TestCase):

    def test_constructor_unavailable_file(self):
        userCategories = ucm.UserCategoriesMemory('unknown.csv')
        os.remove('unknown.csv')
        self.assertEqual(userCategories.status, True)

    def test_constructor_correct_file(self):
        userCategories = ucm.UserCategoriesMemory('data/user_categories_mem_test_file.csv')
        self.assertEqual(userCategories.status, False)
        self.assertEqual(len(userCategories.income_categories), 4)
        self.assertEqual(len(userCategories.expense_categories), 4)

    def test_removeDeprecatedCategories_wrong_HomeBankObject(self):
        userCat = ucm.UserCategoriesMemory('data/user_categories_mem_test_file.csv')
        self.assertRaises(Exception, userCat.removeDeprecatedCategories, 'None', ';')

    def test_removeDeprecatedCategories(self):
        copyfile('data/user_categories_mem_test_file.csv',
                 'data/user_categories_mem_test_file.csv.orig')
        homeBankCat = hbc.HomeBankCategories('data/homebank_test_file.xhb')
        userCat = ucm.UserCategoriesMemory('data/user_categories_mem_test_file.csv')
        userCat.removeDeprecatedCategories(homeBankCat)
        self.assertEqual(len(userCat.income_categories), 3)
        self.assertEqual(len(userCat.expense_categories), 3)
        copyfile('data/user_categories_mem_test_file.csv',
                 'data/updated.csv')
        copyfile('data/user_categories_mem_test_file.csv.orig',
                 'data/user_categories_mem_test_file.csv')
        os.remove('data/user_categories_mem_test_file.csv.orig')
        userCategories = ucm.UserCategoriesMemory('data/updated.csv')
        self.assertEqual(userCategories.status, False)
        self.assertEqual(len(userCategories.income_categories), 3)
        self.assertEqual(len(userCategories.expense_categories), 3)
        os.remove('data/updated.csv')

    def test_addNew_wrong_UserCategoryObject(self):
        userCat = ucm.UserCategoriesMemory('data/user_categories_mem_test_file.csv')
        self.assertRaises(Exception, userCat.addNew, 'None', ';')

    def test_addNew_(self):
        copyfile('data/user_categories_mem_test_file.csv',
                 'data/user_categories_mem_test_file.csv.orig')
        userCatMem = ucm.UserCategoriesMemory('data/user_categories_mem_test_file.csv')
        userCat = uc.UserCategory('Token9;-;Category9', ';')
        userCatMem.addNew(userCat, ';')
        copyfile('data/user_categories_mem_test_file.csv',
                 'data/updated.csv')
        copyfile('data/user_categories_mem_test_file.csv.orig',
                 'data/user_categories_mem_test_file.csv')
        os.remove('data/user_categories_mem_test_file.csv.orig')
        userCategories = ucm.UserCategoriesMemory('data/updated.csv')
        self.assertEqual(userCategories.status, False)
        self.assertEqual(len(userCategories.income_categories), 4)
        self.assertEqual(len(userCategories.expense_categories), 5)
        os.remove('data/updated.csv')

    def test_findCategory(self):
        userCategories = ucm.UserCategoriesMemory('data/user_categories_mem_test_file.csv')
        self.assertEqual(userCategories.status, False)
        self.assertEqual(userCategories.findCategory("-", "Token2"), "Category2")
        self.assertEqual(userCategories.findCategory("+", "Token2"), "")
        self.assertEqual(userCategories.findCategory("+", "Token3"), "Category3")


if __name__ == "__main__":

    unittest.main()
