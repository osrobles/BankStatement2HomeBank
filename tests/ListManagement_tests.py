#!/usr/bin/python3
"""
    ListManagement module tests
    2022-11-16 18:44
"""

import unittest
from unittest.mock import patch
from context import ListManagement


class Test(unittest.TestCase):

    empty_list = []
    test_list = ["uno", "dos", "tres", "cuatro", "cinco"]
    test_csv = "uno;dos;tres;cuatro;cinco"

    def test_ask_user_for_list_items_empty(self):
        out = ListManagement.ask_user_for_list_items(Test.empty_list, False)
        self.assertEqual(out, "")

    @patch('builtins.input', lambda *args: '1')
    def test_ask_user_for_list_items_one_item(self):
        out = ListManagement.ask_user_for_list_items(Test.test_list, False)
        self.assertEqual(out, "uno")

    @patch('builtins.input', lambda *args: '2,4')
    def test_ask_user_for_list_items_several_items(self):
        out = ListManagement.ask_user_for_list_items(Test.test_list, True)
        self.assertEqual(out, "dos cuatro")

    def test_list2csv_empty(self):
        out = ListManagement.list2csv(Test.empty_list)
        self.assertEqual(out, "")

    def test_list2csv_correct(self):
        out = ListManagement.list2csv(Test.test_list, ";")
        self.assertEqual(out, Test.test_csv)

    def test_csv2list_empty(self):
        out = ListManagement.csv2list("")
        self.assertEqual(len(out), 0)

    def test_csv2list_correct(self):
        out = ListManagement.csv2list(Test.test_csv, ";")
        print(f'out: {out}')
        self.assertEqual(out, Test.test_list)


if __name__ == "__main__":

    unittest.main()
