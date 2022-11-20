#!/usr/bin/python3
"""
    Transaction module
    2022-11-20 14:32
"""

from datetime import datetime
from enum import IntEnum
import ListManagement as ListMgmt
import HomeBankPaymentModes as HBModes


def dateString2datetime(date=""):
    """
    !@brief This converts a date string to a datetime object

    @param date         - date string

    return datetime object
    """
    if not isinstance(date, str) or len(date) == 0:
        raise Exception("ERROR: date type/len")

    date_sample = date.split(" ")[0]
    date_sep = ""
    for c in date_sample:
        if not c.isnumeric():
            date_sep = c

    date_numbers = date_sample.split(date_sep)
    if int(date_numbers[0]) > 31:
        date_format = f'%Y{date_sep}%m{date_sep}%d'
    else:
        date_format = f'%d{date_sep}%m{date_sep}%Y'

    return datetime.strptime(date.split(" ")[0], date_format).date()


class CSVInfoIndex(IntEnum):
    """
    Category CSV Info Index enumerate
    """
    TOKEN = 0
    MODE = 1
    TOTAL = 2


class Transaction():
    """
        Class with transaction information
    """

    def __init__(self, date="1970/01/01", payment_mode=HBModes.PaymentModesEnum.NONE,
                 info="", payee="", memo="", amount=0, category="", tags=""):
        """
        !@brief This function creates a new transaction object

        @param date         - transaction date (required)
        @param payment_mode - transaction payment mode
        @param info         - transaction info
        @param payee        - transaction payee
        @param memo         - transaction memo
        @param amount       - transaction amount (required)
        @param category     - transaction category
        @param tags         - transaction tags

        """
        self.date = dateString2datetime(date)

        if not isinstance(payment_mode, int):
            raise Exception("ERROR: MODE type")
        elif payment_mode not in HBModes.getValueList():
            raise Exception("ERROR: MODE unknown")
        else:
            self.mode = payment_mode

        if not isinstance(info, str):
            raise Exception("ERROR: info type")
        else:
            self.info = info

        if not isinstance(payee, str):
            raise Exception("ERROR: payee type")
        else:
            self.payee = payee

        if not isinstance(memo, str):
            raise Exception("ERROR: memo type")
        else:
            self.memo = memo

        if not isinstance(amount, int) and not isinstance(amount, float):
            raise Exception("ERROR: amount type")
        else:
            self.amount = amount

        if not isinstance(category, str):
            raise Exception("ERROR: category type")
        else:
            self.category = category

        if not isinstance(tags, str):
            raise Exception("ERROR: tags type")
        else:
            self.tags = tags

    def toCSV(self, sep=";"):
        """
        !@brief This function converts UserCategory fields to CSV format

        @param  sep - separator character

        @return UserCategory CSV string
        """
        return ListMgmt.list2csv(list(self.__dict__.values()), sep)
