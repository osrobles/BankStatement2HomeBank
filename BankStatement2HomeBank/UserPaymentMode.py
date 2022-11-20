#!/usr/bin/python3
"""
    UserPaymentMode module
    2022-11-19 00:31
"""

from enum import IntEnum
import ListManagement as ListMgmt
import HomeBankPaymentModes as HBModes


class CSVInfoIndex(IntEnum):
    """
    Category CSV Info Index enumerate
    """
    TOKEN = 0
    MODE = 1
    TOTAL = 2


class UserPaymentMode():
    """
        Class with user payment modes information
    """

    def __init__(self, csv_string='', sep=";"):
        """
        !@brief This function creates a new custom categories object

        @param csv_string   - CSV string with the payment modes information (token;mode)

        @param  sep         - separator character
        """
        if not isinstance(csv_string, str) or len(csv_string) == 0:
            raise Exception("ERROR: csv_string type/len")
        else:
            cat_info = ListMgmt.csv2list(csv_string, ";")

        if len(cat_info) < CSVInfoIndex.TOTAL:
            raise Exception("ERROR: csv_string number of fields")

        token = cat_info[CSVInfoIndex.TOKEN.value]
        if not isinstance(token, str) or len(token) == 0:
            raise Exception("ERROR: token type/len")
        else:
            self.token = token.lower()

        mode = int(cat_info[CSVInfoIndex.MODE.value])
        if not isinstance(mode, int):
            raise Exception("ERROR: MODE type")
        elif mode not in HBModes.getValueList():
            raise Exception("ERROR: MODE unknown")
        else:
            self.mode = mode

    def checkMembership(self, input_string=""):
        """
        !@brief This function checks if the input string contains the token

        @param string - target mode object

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
