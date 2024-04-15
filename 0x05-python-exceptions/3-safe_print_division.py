#!/usr/bin/python3
"""Defines a division module"""


def safe_print_division(a, b):
    """
    Divides two integers and prints the result.

    Parameters:
        a (int): The dividend.
        b (int): The divisor.

    Returns:
        float or None:
    """
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        if result is not None:
            print("Inside result : {:.1f}".format(result))
        else:
            print("Inside result : None")
    return result
