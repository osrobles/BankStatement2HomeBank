#!/usr/bin/python3
"""
    Resources for user categories memory management
    2022-11-16 22:11
"""

import UserCategory
import HomeBankCategories


def parse_file(file_path, separator=";",
               income_category_list=[], expense_category_list=[]):
    """
    !@brief This function parses an user categories memory file

        @param  file_path               - file path
        @param  separator               - CSV separator
        @param  income_category_list    - income categories list
        @param  expense_category_list   - expense categories list

        @return Status (OK = False, Empty file = True)
    """
    try:
        fin = open(file_path, 'r')
    except IOError:
        print(f'File {file_path} does not exist. It has been created')
        fin = open(file_path, 'w')
        fin.close()
        return True

    for line in fin.read().splitlines():
        uc = UserCategory.UserCategory(line, separator)
        if uc.sign == "-":
            expense_category_list.append(uc)
        elif uc.sign == "+":
            income_category_list.append(uc)
    fin.close()
    return False


class UserCategoriesMemory():
    """
        Class for User Category Memory
    """

    def __init__(self, file_path='', separator=";"):
        """
        !@brief This function creates a new HomeBank categories object

        @param file_path - HomeBank file (.xhb)
        """
        self.file_path = file_path
        self.expense_categories = []
        self.income_categories = []
        self.status = parse_file(file_path, separator,
                                 self.income_categories,
                                 self.expense_categories)

    def removeDeprecatedCategories(self, HomeBankCategoriesObject=None, sep=";"):
        """
        !@brief This function removes user category which contains deprecated category names

        @param HomeBankCategoriesObject - HomeBankCategories object
        @param sep                      - separator character
        """
        if not isinstance(HomeBankCategoriesObject, HomeBankCategories.HomeBankCategories):
            raise Exception("ERROR: HomeBankCategoriesObject")

        for i, cat in enumerate(self.expense_categories):
            if cat.category_name not in HomeBankCategoriesObject.expense_categories:
                self.expense_categories.pop(i)
        for i, cat in enumerate(self.income_categories):
            if cat.category_name not in HomeBankCategoriesObject.income_categories:
                self.income_categories.pop(i)
        self.write2file(sep)

    def write2file(self, sep=";"):
        """
        !@brief This function writes the object contents to file in CSV format

        @param  sep - separator character
        """
        fout = open(self.file_path, "w")
        for uc in self.expense_categories:
            fout.write(uc.toCSV(sep) + '\n')
        for uc in self.income_categories:
            fout.write(uc.toCSV(sep) + '\n')
        fout.close()

    def addNew(self, UserCategoryObject=None, sep=";"):
        """
        !@brief This function adds new UserCategory and appends it to the file

        @param UserCategoryObject   - HomeBankCategories object
        @param sep                  - separator character
        """
        if not isinstance(UserCategoryObject, UserCategory.UserCategory):
            raise Exception("ERROR: UserCategoryObject")
        append = True
        if UserCategoryObject.sign == '-':
            self.expense_categories.append(UserCategoryObject)
        elif UserCategoryObject.sign == '+':
            self.income_categories.append(UserCategoryObject)
        else:
            append = False
        if append:
            fout = open(self.file_path, "a")
            fout.write(UserCategoryObject.toCSV(sep) + '\n')
            fout.close()

    def findCategory(self, sign='-', token=""):
        """
        !@brief This function checks if object already contains a category

        @param sign     - category sign (+, -)
        @param token    - Token string to compare

        @return False or True
        """
        if not isinstance(token, str) or len(token) == 0:
            raise Exception("ERROR: token")
        category = ""
        if sign == '-':
            for uc in self.expense_categories:
                if uc.checkMembership(token):
                    category = uc.category_name
                    break
        elif sign == "+":
            for uc in self.income_categories:
                if uc.checkMembership(token):
                    category = uc.category_name
                    break
        return category
