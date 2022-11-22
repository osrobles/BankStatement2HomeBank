#!/usr/bin/python3
"""
    BankFormatManager module tests
    2022-11-22 23:09
"""

import unittest
from context import BankFormatManager as BFM


class Test(unittest.TestCase):

    def test_file_wrong_type(self):
        self.assertRaises(Exception, BFM.BankFormatManager, 5)

    def test_file_wrong_ext(self):
        self.assertRaises(Exception, BFM.BankFormatManager, 'test.csv')

    def test_file_unknown(self):
        self.assertRaises(Exception, BFM.BankFormatManager, 'unknown.xml')

    def test_file_ok(self):
        ids = BFM.BankFormatManager('data/bank_format_file.xml')
        self.assertEqual(ids.bank_format_ids.date, 'Date')
        self.assertEqual(ids.bank_format_ids.amount, 'Amount')
        self.assertEqual(ids.bank_format_ids.concept, 'Concept')
        self.assertEqual(ids.bank_format_ids.movement, 'Movement')


if __name__ == "__main__":

    unittest.main()
