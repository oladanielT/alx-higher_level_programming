#!/usr/bin/python3
"""Defines a module"""


def safe_print_integer(value):
    printed = False
    try:
        if isinstance(value, int):
            print("{:d}".format(value), end="")
            printed = True
    except TypeError:
        printed = False
        pass
    print()
    return printed
