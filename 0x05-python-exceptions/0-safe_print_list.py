#!/usr/bin/python3
"""Defines a module to print from a list"""


def safe_print_list(my_list=[], x=0):
    """
    Defines the function.
    Parameters:
        my_list (int or str) : list of integers
        x (int): length of elemnt to print.
    Return:
        items in my _list of length lesser than x.
        length of items.
    Raises:
        IndexError: x must not be greater than len(my_list).
    """
    printed = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end=" ")
            printed += 1
    except IndexError:
        pass
    else:
        print()
    return printed
