#!/usr/bin/python3
"""
    UserPaymentMode module
    2022-11-19 00:31
"""

from enum import IntEnum
import ListManagement as ListMgmt


class CSVInfoIndex(IntEnum):
    """
    Category CSV Info Index enumerate
    """
    TOKEN = 0
    MODE = 1
    TOTAL = 2


class PaymentModes(IntEnum):
    """
    Payment modes enumerate
    """
    NONE = 0
    CREDIT_CARD = 1
    CHECK = 2
    CASH = 3
    BANK_TRANSFER = 4
    DEBIT_CARD = 6
    STANDING_ORDER = 7
    ELECTRONIC_PAYMENT = 8
    DEPOSIT = 9
    FIF = 10
    DIRECT_DEBIT = 11


class UserPaymentMode():
    """
        Class with user payment modes information
    """

    paymentModes = {"Ninguno":  PaymentModes.NONE.value,
                    "Tarjeta de crédito": PaymentModes.CREDIT_CARD.value,
                    "Cheque": PaymentModes.CHECK.value,
                    "Efectivo": PaymentModes.CASH.value,
                    "Transferencia bancaria": PaymentModes.BANK_TRANSFER.value,
                    "Tarjeta de débito": PaymentModes.DEBIT_CARD.value,
                    "Orden de posición": PaymentModes.STANDING_ORDER.value,
                    "Pago electrónico": PaymentModes.ELECTRONIC_PAYMENT.value,
                    "Depósito": PaymentModes.DEPOSIT.value,
                    "FIF": PaymentModes.FIF.value,
                    "Cargo directo": PaymentModes.DIRECT_DEBIT.value}
    paymentModesList = list(paymentModes)

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

        mode_list = [item.value for item in PaymentModes]
        mode = int(cat_info[CSVInfoIndex.MODE.value])
        if not isinstance(mode, int):
            raise Exception("ERROR: MODE type")
        elif mode not in mode_list:
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
