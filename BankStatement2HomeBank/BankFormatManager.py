#!/usr/bin/python3
"""
    BankFormatManager module
    2022-11-22 23:00
"""
import os
import xml.etree.ElementTree as ET
import CommonFunctions as CF
from dataclasses import dataclass


@dataclass
class BankFormatIDs:
    """
    Bank format fields
    """
    date: str = ""
    amount: str = ""
    concept: str = ""
    movement: str = ""


class BankFormatManager():
    """
        Class with bank format information
    """

    def __init__(self, bank_format_file=""):
        """
        !@brief This function creates a new transaction list object

        @param bank_format_file     - bank format file with transaction fields names (XML)

        """
        if not os.path.isfile(bank_format_file):
            raise Exception("ERROR: file_path does not exist")
        CF.checkFileInputParam(bank_format_file, ['xml'])
        tree = ET.parse(bank_format_file)
        root = tree.getroot()
        self.bank_format_ids = BankFormatIDs()
        self.bank_format_ids.date = root.find('date_id').text
        self.bank_format_ids.amount = root.find('amount_id').text
        self.bank_format_ids.concept = root.find('concept_id').text
        self.bank_format_ids.movement = root.find('movement_id').text
