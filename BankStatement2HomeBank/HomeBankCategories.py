#!/usr/bin/python3
"""
    Resources for HomeBank original file (.xhb) categories extraction
    2022-08-31 23:38
"""


def extract_field(line, field):
    """
        !@brief This function extracts a field from a line whose fields
                are formatted as field=""

        @param line     - line
        @param field    - field to extract
    """
    word_list = line.split('"')
    for w_index, word in enumerate(word_list):
        if word.find(field) != -1:
            return word_list[w_index + 1]
    return ""


def parse_category_list(file_path, income_category_list,
                        expense_category_list):
    """
    !@brief This function parses a homebank file

        @param  file_path               - file path
        @param  income_category_list    - income categories list
        @param  expense_category_list   - expense categories list

        @return Status (OK = False, NOK = True)
    """
    try:
        fin = open(file_path, 'r')
    except IOError:
        print(f'HomeBank file {file_path} does not exist')
        return True

    for line in fin:

        # Get only category lines
        if line[0:4] == "<cat":

            # Get flags
            flags = extract_field(line, "flags")

            # Build category
            if flags == "":
                parent = extract_field(line, "name")
                expense_category_list.append(parent)
            elif flags == "1":
                expense_category_list.append(parent + ":" +
                                             extract_field(line, "name"))
            elif flags == "2":
                parent = extract_field(line, "name")
                income_category_list.append(parent)
            elif flags == "3":
                income_category_list.append(parent + ":" +
                                            extract_field(line, "name"))
    fin.close()
    expense_category_list.sort()
    if len(expense_category_list) == 0:
        print("Expense category list empty")
    income_category_list.sort()
    if len(income_category_list) == 0:
        print("Income category list empty")
    return False


class HomeBankCategories():
    """
        Class with HomeBank categories information
    """

    def __init__(self, file_path=''):
        """
        !@brief This function creates a new HomeBank categories object

        @param file_path - HomeBank file (.xhb)
        """
        self.expense_categories = []
        self.income_categories = []
        self.status = parse_category_list(file_path, self.income_categories,
                                          self.expense_categories)

    def contains(self, sign='income', category=""):
        """
        !@brief This function checks if object already contains a category

        @param sign             - category sign (income, expense)
        @param category         - target category object

        @return False or True
        """
        if sign == 'income':
            return (category in self.income_categories)
        else:
            return (category in self.expense_categories)
