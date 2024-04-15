#!/usr/bin/python3
"""Defines a modules"""


def list_division(my_list_1, my_list_2, list_length):
    """
    Reperesents a function to divides item of list1 from item of list2.

    Parameters:
        my_list_1 (int, str): first list.
        my_list_2 (int, str): second list.
    Raises:
        TyperError:
        ZeroDivisionError:
    """
    result = []
    for i in range(list_length):
        try:
            if not isinstance(my_list_1[i], (int, float)) or not isinstance(my_list_2[i], (int, float)):
                raise TypeError("wrong type")
            if my_list_2[i] == 0:
                raise ZeroDivisionError("division by 0")
            result.append(my_list_1[i] / my_list_2[i])
        except TypeError:
            print("wrong type")
            result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
    return result
