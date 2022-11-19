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

    homebank_file_path = 'data/homebank_test_file.xhb'
    unknown_path = 'data/unknown.csv'
    test_file_path = 'data/user_categories_mem_test_file.csv'
    orig_file_path = 'data/user_categories_mem_test_file.csv.orig'
    update_file_path = 'data/update.csv'

    def test_constructor_unavailable_file(self):
        userCategories = ucm.UserCategoriesMemory(Test.unknown_path)
        os.remove(Test.unknown_path)
        self.assertEqual(userCategories.status, True)

    def test_constructor_correct_file(self):
        userCategories = ucm.UserCategoriesMemory(Test.test_file_path)
        self.assertEqual(userCategories.status, False)
        self.assertEqual(len(userCategories.income_categories), 4)
        self.assertEqual(len(userCategories.expense_categories), 4)

    def test_removeDeprecatedCategories_wrong_HomeBankObject(self):
        userCat = ucm.UserCategoriesMemory(Test.test_file_path)
        self.assertRaises(Exception, userCat.removeDeprecatedCategories, 'None', ';')

    def test_removeDeprecatedCategories(self):
        copyfile(Test.test_file_path, Test.orig_file_path)
        homeBankCat = hbc.HomeBankCategories(Test.homebank_file_path)
        userCat = ucm.UserCategoriesMemory(Test.test_file_path)
        userCat.removeDeprecatedCategories(homeBankCat)
        self.assertEqual(len(userCat.income_categories), 3)
        self.assertEqual(len(userCat.expense_categories), 3)
        copyfile(Test.test_file_path, Test.update_file_path)
        copyfile(Test.orig_file_path, Test.test_file_path)
        os.remove(Test.orig_file_path)
        userCategories = ucm.UserCategoriesMemory(Test.update_file_path)
        self.assertEqual(userCategories.status, False)
        self.assertEqual(len(userCategories.income_categories), 3)
        self.assertEqual(len(userCategories.expense_categories), 3)
        os.remove(Test.update_file_path)

    def test_addNew_wrong_UserCategoryObject(self):
        userCat = ucm.UserCategoriesMemory(Test.test_file_path)
        self.assertRaises(Exception, userCat.addNew, 'None', ';')

    def test_addNew_correct(self):
        copyfile(Test.test_file_path, Test.orig_file_path)
        userCatMem = ucm.UserCategoriesMemory(Test.test_file_path)
        userCat = uc.UserCategory('Token9;-;Category9', ';')
        userCatMem.addNew(userCat, ';')
        copyfile(Test.test_file_path, Test.update_file_path)
        copyfile(Test.orig_file_path, Test.test_file_path)
        os.remove(Test.orig_file_path)
        userCategories = ucm.UserCategoriesMemory(Test.update_file_path)
        self.assertEqual(userCategories.status, False)
        self.assertEqual(len(userCategories.income_categories), 4)
        self.assertEqual(len(userCategories.expense_categories), 5)
        os.remove(Test.update_file_path)

    def test_findCategory(self):
        userCategories = ucm.UserCategoriesMemory(Test.test_file_path)
        self.assertEqual(userCategories.status, False)
        self.assertEqual(userCategories.findCategory("-", "Token2"), "Category2")
        self.assertEqual(userCategories.findCategory("+", "Token2"), "")
        self.assertEqual(userCategories.findCategory("+", "Token3"), "Category3")


if __name__ == "__main__":

    unittest.main()
