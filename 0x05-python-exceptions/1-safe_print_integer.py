#!/usr/bin/python3
"""Defines a module"""


def safe_print_integer(value):
    try:
        if isinstance(value, int):
            print("{:d}".format(value), end="")
            print()
            return True
    except TypeError:
        pass
    return False
