"""
    Resources for HomeBank original file (.xhb) categories extraction
    2022-08-31 23:38
"""

"""
Functions
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

    """
    try:
        fin = open(file_path, 'r')
    except IOError:
        print(f'HomeBank file {file_path} does not exist')
        return

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
    expense_category_list.sort()
    income_category_list.sort()


"""
Classes
"""


class HomeBankCategory():
    """
        Class with HomeBank category information
    """

    def __init__(self, sign='income', category="", subcategory=""):
        """
        !@brief Creates a new HomeBank category

        @param sign         - category sign (income, expense)
        @param category     - category string
        @param subcategory  - subcategory string
        """
        if sign != "income":
            self.sign = "expense"
        else:
            self.sign = sign
        self.category = category
        self.subcategory = subcategory

    def compare(self, target):
        """
        !@brief This function compares two HomeBank categories

        @param target   - target category object

        @return False or True
        """
        return ((self.sign == target.sign) and
                (self.category == target.category) and
                (self.subcategory == target.subcategory))


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
        parse_category_list(file_path, self.income_categories,
                            self.expense_categories)


if __name__ == "__main__":

    category1 = HomeBankCategory("income", "testcat", "testsubcat")
    category2 = HomeBankCategory("expense", "testcat", "testsubcat")
    category3 = HomeBankCategory("income", "testcat", "testsubcat")

    print(f'Test1: {category1.compare(category2)}')
    print(f'Test2: {category1.compare(category3)}')

    hbcategories = HomeBankCategories('est.xhb')
    print("Income categories:")
    print(hbcategories.income_categories)
    print("Expense categories:")
    print(hbcategories.expense_categories)
