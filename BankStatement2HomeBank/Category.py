#!/usr/bin/python3
"""
    Category module
    2022-11-08 23:59
"""


class Category():
    """
        Class with custom categories information
    """

    def __init__(self, token='', category_name=''):
        """
        !@brief This function creates a new custom categories object

        @param token            - token ID for the category
        @param category_name    - category name assigned to the token
        """
        if not isinstance(token, str) or len(token) == 0:
            raise Exception("ERROR: token")
        else:
            self.token = token.lower()
        if not isinstance(category_name, str) or len(category_name) == 0:
            raise Exception("ERROR: category name")
        else:
            self.category_name = category_name

    def checkMembership(self, input_string=""):
        """
        !@brief This function checks if the input string contains the token

        @param string - target category object

        @return False or True
        """
        return (self.token in input_string.lower())


if __name__ == "__main__":

    cat = Category('test', 'test')
    print(f'1: {cat.check("My test")}')
    print(f'1: {cat.check("Hola")}')
