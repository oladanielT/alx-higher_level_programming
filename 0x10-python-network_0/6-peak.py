#!/usr/bin/python3
# a function that finds a peak in a list of unsorted integer


def find_peak(list_of_integers):
    """function to find the peak of a list"""
    if list_of_integers == []:
        return (None)
    
    list_len = len(list_of_integers)
    if (list_len == 0):
        return (None)
    elif (list_len == 1):
        return (list_of_integers[0])
    elif (list_len == 2):
        return (max(list_of_integers))

    my_list = list_of_integers
    mid = int(list_len/2)
    peak = my_list[mid]
    if (peak > my_list[mid - 1] and peak > my_list[mid + 1]):
        return (my_list[mid])
    elif (peak < my_list[mid - 1]):
        return (find_peak(my_list[:mid]))
    else:
        return (find_peak(my_list[mid + 1:]))
