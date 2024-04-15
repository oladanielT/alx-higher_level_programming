#!/usr/bin/python3
"""Defines a module"""


def safe_print_list_integers(my_list=[], x=0):
    """Represent a function that print an integer

    Parameters:
        my_list (int or str): list of items.
        x (int): size of element to print.
    Raises:
        IndexError: when x is greater than the length of my_list.
    """
    printed = 0
    try:
        for value in my_list:
            if isinstance(value, int):
                print("{:d}".format(value), end="")
                printed += 1
                if printed >= x:
                    break
    except IndexError:
        pass
    print()
    return printed
