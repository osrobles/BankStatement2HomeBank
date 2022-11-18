#!/usr/bin/python3
"""
    Context for tests
    2022-09-01 23:07
"""
import os
import sys

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, path)
path = path + '/BankStatement2HomeBank'
sys.path.insert(0, path)


import ListManagement
import HomeBankCategories
import UserCategory
import UserCategoriesMemory
