#!/usr/bin/python3
"""
    UserCategory module
    2022-11-08 23:59
"""

from enum import IntEnum
import ListManagement as ListMgmt


class CSVInfoIndex(IntEnum):
    """
    Category CSV Info Index enumerate
    """
    TOKEN = 0
    SIGN = 1
    CATEGORY = 2
    TOTAL = 3


class UserCategory():
    """
        Class with custom categories information
    """

    def __init__(self, csv_string='', sep=";"):
        """
        !@brief This function creates a new custom categories object

        @param csv_string   - CSV string with the category information (token:sign:category_name)

        @param  sep         - separator character
        """
        if not isinstance(csv_string, str) or len(csv_string) == 0:
            raise Exception("ERROR: csv_string")
        else:
            cat_info = ListMgmt.csv2list(csv_string, ";")

        if len(cat_info) < CSVInfoIndex.TOTAL.value:
            raise Exception("ERROR: csv_string number of fields")

        token = cat_info[CSVInfoIndex.TOKEN.value]
        if not isinstance(token, str) or len(token) == 0:
            raise Exception("ERROR: token")
        else:
            self.token = token.lower()

        sign = cat_info[CSVInfoIndex.SIGN.value]
        if sign == '-' or sign == '+':
            self.sign = sign
        else:
            raise Exception(f'ERROR: sign {sign} not allowed')

        category_name = cat_info[CSVInfoIndex.CATEGORY.value]
        if not isinstance(category_name, str) or len(category_name) == 0:
            raise Exception("ERROR: category name")
        else:
            self.category_name = category_name

    def checkMembership(self, input_string=""):
        """
        !@brief This function checks if the input string contains the token

        @param string - target category object

        @return False or True
        """
        return (self.token in input_string.lower())

    def toCSV(self, sep=";"):
        """
        !@brief This function converts UserCategory fields to CSV format

        @param  sep - separator character

        @return UserCategory CSV string
        """
        return ListMgmt.list2csv(list(self.__dict__.values()), sep)
