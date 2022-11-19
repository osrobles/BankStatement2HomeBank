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

    test_file_path = 'data/user_modes_mem_test_file.csv'
    def test_constructor_unavailable_file(self):
        userModesMem = umm.UserPaymentModesMemory('unknown.csv')
        os.remove('unknown.csv')
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
        userModesMem = umm.UserPaymentModesMemory('data/user_modes_mem_test_file.csv')
        self.assertRaises(Exception, userModesMem.addNew, 'None', ';')

    def test_addNew_correct(self):
        copyfile('data/user_modes_mem_test_file.csv', 'data/user_modes_mem_test_file.csv.orig')
        userModesMem = umm.UserPaymentModesMemory('data/user_modes_mem_test_file.csv')
        userMode = um.UserPaymentMode('Token9;1', ';')
        userModesMem.addNew(userMode, ';')
        copyfile('data/user_modes_mem_test_file.csv', 'data/updated.csv')
        copyfile('data/user_modes_mem_test_file.csv.orig', 'data/user_modes_mem_test_file.csv')
        os.remove('data/user_modes_mem_test_file.csv.orig')
        userModesMem = umm.UserPaymentModesMemory('data/updated.csv')
        self.assertEqual(userModesMem.status, False)
        self.assertEqual(len(userModesMem.modes_memory), 11)
        os.remove('data/updated.csv')

    def test_findMode(self):
        userModesMem = umm.UserPaymentModesMemory('data/user_modes_mem_test_file.csv')
        self.assertEqual(userModesMem.status, False)
        self.assertEqual(userModesMem.findMode("Token2"), 2)
        self.assertEqual(userModesMem.findMode("Token3"), 3)


if __name__ == "__main__":

    unittest.main()
