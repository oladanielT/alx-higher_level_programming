#!/usr/bin/python3
# a function that finds a peak in a list of unsorted integers.

def find_peak(list_of_integers):
    """The function to find peak"""
    if list_of_integers == []:
        return (None)
    my_list = list_of_integers
    list_len = len(my_list)
    if list_len == 0:
        return (None)
    elif list_len == 1:
        return my_list[0]
    elif list_len == 2:
        return max(my_list)
    mid = int(list_len/2)
    if my_list[mid] > my_list[mid - 1] and my_list[mid] > my_list[mid + 1]:
        return (my_list[mid])
    elif my_list[mid] < my_list[mid - 1]:
        return (find_peak(my_list[:mid]))
    else:
        return (find_peak(my_list[mid + 1:]))
