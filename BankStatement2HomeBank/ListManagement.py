#!/usr/bin/python3
"""
    Resources for list management and display
    2022-11-12 16:43
"""


def ask_user_for_list_items(lst, multiple_index_enable=False):
    """
    !@brief This function which ask user to choose an index or a list of index
            from a list. The function return an string with the list words
            separated by commas

        @param  lst - list
        @param  multiple_index_enable - multiple index flag

        @return String with selected items
    """
    if len(lst) == 0:
        print("WARNING! Empty list")
        return ""
    while True:
        print("Please, choose an option or a list of options separated by commas")
        for index, item in enumerate(lst, 1):
            print(f'[{index}]\t{item}')
        index_list = input().split(',')
        outtext = ""
        error_found = False
        for i in index_list:
            try:
                outtext += lst[int(i) - 1]
                if not multiple_index_enable:
                    break
                if i != index_list[-1]:
                    outtext += " "
            except ValueError:
                print("Index must be a number")
                error_found = True
                break
            except IndexError:
                print(f'Index {i} out of bounds')
                error_found = True
                break

        if not error_found:
            break

    return outtext[0:len(outtext)]


def list2csv(lst, sep=";"):
    """
    !@brief This function converts a list to a csv string

        @param  lst - list
        @param  sep - separator character

        @return CSV string
    """
    csv_str = ""
    for index, item in enumerate(lst):
        if index == len(lst) - 1:
            csv_str += f'{item}'
        else:
            csv_str += f'{item}{sep}'
    return csv_str


def csv2list(csvString="", sep=";"):
    """
    !@brief This function converts a CSV string to a list

        @param  csvString   - CSV string
        @param  sep         - separator character

        @return List with seperated CSV fields
    """
    if not isinstance(csvString, str) or len(csvString) == 0:
        return []
    return csvString.split(sep)
