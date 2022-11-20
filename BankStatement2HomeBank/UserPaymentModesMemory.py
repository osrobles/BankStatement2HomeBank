#!/usr/bin/python3
"""
    Resources for user payment modes memory management
    2022-11-19 16:13
"""

import HomeBankPaymentModes as HBModes
import UserPaymentMode


def parse_file(file_path, separator=";",
               card_mode=HBModes.PaymentModesEnum.DEBIT_CARD,
               modes_list=[]):
    """
    !@brief This function parses an user pyament modes memory file

        @param  file_path   - file path
        @param  separator   - CSV separator
        @param  card_mode   - Card mode for card operations
        @param  modes_list  - payment modes list

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
        upm = UserPaymentMode.UserPaymentMode(line, separator)
        if upm.mode == HBModes.PaymentModesEnum.DEBIT_CARD or \
           upm.mode == HBModes.PaymentModesEnum.CREDIT_CARD:
            upm.mode = card_mode
        modes_list.append(upm)
    fin.close()
    return False


class UserPaymentModesMemory():
    """
        Class for User Payment Modes Memory
    """

    def __init__(self, file_path='', separator=";", card_type="debit"):
        """
        !@brief This function creates a new HomeBank categories object

        @param file_path    - User payment modes memory file (.csv)
        @param sep          - separator character
        @param card_type    - Default card type (debit, credit)
        """
        self.file_path = file_path
        self.modes_memory = []
        if not isinstance(card_type, str) or \
           (card_type.lower() not in (["debit", "credit"])):
            print(f'WARNING: unknown card_type {card_type}')
            self.card_type = HBModes.PaymentModesEnum.DEBIT_CARD
        elif card_type == "debit":
            self.card_type = HBModes.PaymentModesEnum.DEBIT_CARD
        else:
            self.card_type = HBModes.PaymentModesEnum.CREDIT_CARD
        self.status = parse_file(file_path, separator,
                                 self.card_type, self.modes_memory)

    def write2file(self, sep=";"):
        """
        !@brief This function writes the object contents to file in CSV format

        @param  sep - separator character
        """
        fout = open(self.file_path, "w")
        for um in self.modes_memory:
            fout.write(um.toCSV(sep) + '\n')
        fout.close()

    def addNew(self, UserPaymentModeObject=None, sep=";"):
        """
        !@brief This function adds new UserPaymentMode and appends it to the file

        @param UserPaymentModeObject    - UserPaymentMode object
        @param sep                      - separator character
        """
        if not isinstance(UserPaymentModeObject, UserPaymentMode.UserPaymentMode):
            raise Exception("ERROR: UserPaymentModeObject")
        self.modes_memory.append(UserPaymentModeObject)
        fout = open(self.file_path, "a")
        fout.write(UserPaymentModeObject.toCSV(sep) + '\n')
        fout.close()

    def findMode(self, token=""):
        """
        !@brief This function finds the token inside the library

        @param token    - Token string to compare

        @return -1 on failure, mode on success
        """
        if not isinstance(token, str) or len(token) == 0:
            raise Exception("ERROR: token")
        mode = -1
        for um in self.modes_memory:
            if um.checkMembership(token):
                mode = um.mode
                break
        return mode
