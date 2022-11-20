#!/usr/bin/python3
"""
    Transaction module tests
    2022-11-20 14:32
"""

import unittest
from context import HomeBankPaymentModes as HBModes
from context import Transaction


class Test(unittest.TestCase):

    test_date = '2022-08-29'
    test_mode = HBModes.PaymentModesEnum.NONE

    def test_date_wrong_type(self):
        self.assertRaises(Exception, Transaction.Transaction, 5)

    def test_date_empty(self):
        self.assertRaises(Exception, Transaction.Transaction, '')

    def test_date_conversion(self):
        t = Transaction.Transaction(date="29/08/2022 12:00:00")
        self.assertEqual(str(t.date), Test.test_date)
        t = Transaction.Transaction(date="2022/08/29 12:00:00")
        self.assertEqual(str(t.date), Test.test_date)
        t = Transaction.Transaction(date="29/08/2022")
        self.assertEqual(str(t.date), Test.test_date)
        t = Transaction.Transaction(date="2022/08/29")
        self.assertEqual(str(t.date), Test.test_date)

    def test_mode_wrong_type(self):
        self.assertRaises(Exception, Transaction.Transaction, payment_mode='5')

    def test_mode_out_of_bounds(self):
        self.assertRaises(Exception, Transaction.Transaction, payment_mode=-1)
        self.assertRaises(Exception, Transaction.Transaction,
                          payment_mode=HBModes.PaymentModesEnum.DIRECT_DEBIT + 1)

    def test_mode_ok(self):
        t = Transaction.Transaction(payment_mode=Test.test_mode)
        self.assertEqual(t.mode, Test.test_mode)

    def test_info_wrong_type(self):
        self.assertRaises(Exception, Transaction.Transaction, info=5)

    def test_info_ok(self):
        t = Transaction.Transaction(info='Test')
        self.assertEqual(t.info, "Test")

    def test_payee_wrong_type(self):
        self.assertRaises(Exception, Transaction.Transaction, payee=5)

    def test_payee_ok(self):
        t = Transaction.Transaction(payee='Test')
        self.assertEqual(t.payee, "Test")

    def test_memo_wrong_type(self):
        self.assertRaises(Exception, Transaction.Transaction, memo=5)

    def test_memo_ok(self):
        t = Transaction.Transaction(memo='Test')
        self.assertEqual(t.memo, "Test")

    def test_amount_wrong_type(self):
        self.assertRaises(Exception, Transaction.Transaction, amount='Test')

    def test_amount_ok(self):
        t = Transaction.Transaction(amount=5)
        self.assertEqual(t.amount, 5)
        t = Transaction.Transaction(amount=-5)
        self.assertEqual(t.amount, -5)
        t = Transaction.Transaction(amount=5.0)
        self.assertEqual(t.amount, 5.0)
        t = Transaction.Transaction(amount=-5.0)
        self.assertEqual(t.amount, -5.0)

    def test_category_wrong_type(self):
        self.assertRaises(Exception, Transaction.Transaction, category=5)

    def test_category_ok(self):
        t = Transaction.Transaction(category='Test')
        self.assertEqual(t.category, "Test")

    def test_tags_wrong_type(self):
        self.assertRaises(Exception, Transaction.Transaction, tags=5)

    def test_tags_ok(self):
        t = Transaction.Transaction(tags='Test')
        self.assertEqual(t.tags, "Test")

    def test_toCSV(self):
        t = Transaction.Transaction(date='2022/11/20 23:31', payment_mode=1,
                                    info='info', payee='payee', memo='memo',
                                    amount=5.0, category='category', tags='tags')
        self.assertEqual('2022-11-20;1;info;payee;memo;5.0;category;tags', t.toCSV())


if __name__ == "__main__":

    unittest.main()
