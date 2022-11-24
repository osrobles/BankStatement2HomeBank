#!/usr/bin/python3
"""
    TransactionListManager module
    2022-11-24 22:40
"""

import Transaction as TR
import UserCategoriesMemory as UCM
import UserPaymentModesMemory as UPMM
from dataclasses import dataclass


@dataclass
class ExtendedTransaction:
    """
    Extended Transaction class
    """
    transaction: TR.Transaction
    category_processed: bool = False
    mode_processed: bool = False

    def isProcessed(self) -> bool:
        return (self.category_processed and self.mode_processed)

    def findTransactionCategory(self, categories_mem: UCM.UserCategoriesMemory):
        """
        !@brief This function looks for a category inside a UserCategoriesMemory

        @param  categories_mem  - UserCategoriesMemory object
        """
        if not isinstance(categories_mem, UCM.UserCategoriesMemory):
            raise TypeError("ERROR: categories_mem")

        sign = ['-', '+'][(self.transaction.amount >= 0)]
        category = categories_mem.findCategory(sign, self.transaction.info)
        if len(category) == 0:
            category = categories_mem.findCategory(sign, self.transaction.memo)
        self.transaction.category = category
        self.transaction.category_processed = (len(category) > 0)

    def findTransactionMode(self, modes_mem: UPMM.UserPaymentModesMemory):
        """
        !@brief This function looks for mode inside a UserPaymentModesMemory

        @param  categories_mem  - UserCategoriesMemory object
        """
        if not isinstance(modes_mem, UPMM.UserPaymentModesMemory):
            raise TypeError("ERROR: modes_mem")

        mode = modes_mem.findCategory(self.transaction.info)
        if mode == -1:
            mode = modes_mem.findCategory(self.transaction.memo)
        self.transaction.mode = 0 if mode == -1 else mode
        self.transaction.mode_processed = (mode == -1)


class TransactionList():
    """
        Transaction List Class
    """

    def __init__(self):
        """
        !@brief This function creates a new empty transaction list object
        """
        self.list = [ExtendedTransaction]
        self.processingIndex = 0

    def addNew(self, transaction: ExtendedTransaction):
        if not isinstance(transaction, ExtendedTransaction):
            raise TypeError("ERROR: transaction")
        self.list.append(transaction)

    def process(self, categories_mem: UCM.UserCategoriesMemory,
                modes_mem: UPMM.UserPaymentModesMemory):
        """
        !@brief This function processes list using a UserCategoriesMemory
                and UserPaymentModesMemory object

        @param  categories_mem  - User categories memory object
        @param  modes_mem       - User payment modes memory object
        """
        marked = False
        for i, t in enumerate(self.list):
            t.findTransactionCategory(categories_mem)
            t.findTransactionMode(modes_mem)
            if not t.isProcessed() and not marked:
                self.processingIndex = i

    def write2file(self, filepath: str = "", sep: str = ';'):
        """
        !@brief This function writes list to a CSV file

        @param  file_path   - file path
        @param  sep         - CSV separator character
        """
        fid = open(filepath, 'w')
        for t in self.list:
            fid.write(t.transaction.toCSV(sep) + '\n')
        fid.close()
