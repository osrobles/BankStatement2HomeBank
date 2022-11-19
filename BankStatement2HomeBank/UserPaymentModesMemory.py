#!/usr/bin/python3
"""
    Resources for user payment modes memory management
    2022-11-19 16:13
"""

import UserPaymentMode


def parse_file(file_path, separator=";", modes_list=[]):
    """
    !@brief This function parses an user pyament modes memory file

        @param  file_path               - file path
        @param  separator               - CSV separator
        @param  modes_list    - payment modes list

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
        modes_list.append(UserPaymentMode.UserPaymentMode(line, separator))
    fin.close()
    return False


class UserPaymentModesMemory():
    """
        Class for User Payment Modes Memory
    """

    def __init__(self, file_path='', separator=";"):
        """
        !@brief This function creates a new HomeBank categories object

        @param file_path - HomeBank file (.xhb)
        """
        self.file_path = file_path
        self.modes_memory = []
        self.status = parse_file(file_path, separator, self.modes_memory)

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
