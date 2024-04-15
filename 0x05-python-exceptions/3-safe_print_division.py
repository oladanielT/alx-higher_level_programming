#!/usr/bin/python3
"""Defines a module for division"""


def safe_print_division(a, b):
    """
    Represent function to divide.

    Parameter:
        a (int, float) : dividend.
        b (int or float) : divisor.
    Raises:
        ZeroDivisionError : when divided by zero
    """
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        if result is not None:
            print("Inside result: {:.1f}".format(result))
        else:
            print("Inside result: None")
    return result
