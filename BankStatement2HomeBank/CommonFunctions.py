#!/usr/bin/python3
"""
    File with functions that are common for the whole project
    2022-11-22 22:56
"""

import os


def checkFileInputParam(file_path="", extension=""):
    """
    !@brief This function checks file input parameter integrity and raises an
            exception on error

    @param file_path    - file path
    @param extension    - target extensions list

    """
    if not isinstance(file_path, str):
        raise Exception("ERROR: bank_format_file type")
    file_ext = os.path.basename(file_path).split('.')[1].lower()
    if file_ext not in [x.lower() for x in extension]:
        raise Exception("ERROR: bank_format_file extension")
