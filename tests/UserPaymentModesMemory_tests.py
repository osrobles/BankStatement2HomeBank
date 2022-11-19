#!/usr/bin/python3
"""
    UserPaymentModesMemory module tests
    2022-11-19 16:45
"""

import unittest
import os
from shutil import copyfile
from context import UserPaymentMode as um
from context import UserPaymentModesMemory as umm


class Test(unittest.TestCase):

    unknown_path = 'data/unknown.csv'
    test_file_path = 'data/user_modes_mem_test_file.csv'
    orig_file_path = 'data/user_modes_mem_test_file.csv.orig'
    update_file_path = 'data/update.csv'

    def test_constructor_unavailable_file(self):
        userModesMem = umm.UserPaymentModesMemory(Test.unknown_path)
        os.remove(Test.unknown_path)
        self.assertEqual(userModesMem.status, True)

    def test_constructor_debit_card(self):
        userModesMem = umm.UserPaymentModesMemory(Test.test_file_path, ";", "debit")
        self.assertEqual(userModesMem.status, False)
        self.assertEqual(len(userModesMem.modes_memory), 10)
        self.assertEqual(userModesMem.modes_memory[0].mode, um.PaymentModes.DEBIT_CARD)
        self.assertEqual(userModesMem.modes_memory[4].mode, um.PaymentModes.DEBIT_CARD)

    def test_constructor_credit_card(self):
        userModesMem = umm.UserPaymentModesMemory(Test.test_file_path, ";", "credit")
        self.assertEqual(userModesMem.status, False)
        self.assertEqual(len(userModesMem.modes_memory), 10)
        self.assertEqual(userModesMem.modes_memory[0].mode, um.PaymentModes.CREDIT_CARD)
        self.assertEqual(userModesMem.modes_memory[4].mode, um.PaymentModes.CREDIT_CARD)

    def test_addNew_wrong_UserPaymentModeObject(self):
        userModesMem = umm.UserPaymentModesMemory(Test.test_file_path)
        self.assertRaises(Exception, userModesMem.addNew, 'None', ';')

    def test_addNew_correct(self):
        copyfile(Test.test_file_path, Test.orig_file_path)
        userModesMem = umm.UserPaymentModesMemory(Test.test_file_path)
        userMode = um.UserPaymentMode('Token9;1', ';')
        userModesMem.addNew(userMode, ';')
        copyfile(Test.test_file_path, Test.update_file_path)
        copyfile(Test.orig_file_path, Test.test_file_path)
        os.remove(Test.orig_file_path)
        userModesMem = umm.UserPaymentModesMemory(Test.update_file_path)
        self.assertEqual(userModesMem.status, False)
        self.assertEqual(len(userModesMem.modes_memory), 11)
        os.remove(Test.update_file_path)

    def test_findMode(self):
        userModesMem = umm.UserPaymentModesMemory(Test.test_file_path)
        self.assertEqual(userModesMem.status, False)
        self.assertEqual(userModesMem.findMode("Token2"), 2)
        self.assertEqual(userModesMem.findMode("Token3"), 3)


if __name__ == "__main__":

    unittest.main()
