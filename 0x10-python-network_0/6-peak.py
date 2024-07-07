#!/usr/bin/python3
#A function to return the peak element in a list


def find_peak(list_of_integers):
    """Function to find a peak in a list of unsorted integers."""
    if not list_of_integers:
        return None

    list_len = len(list_of_integers)
    if list_len == 1:
        return list_of_integers[0]
    elif list_len == 2:
        return max(list_of_integers)

    mid = list_len // 2
    peak = list_of_integers[mid]

    # Check if peak is greater than neighbors
    if (peak > list_of_integers[mid - 1]) and (peak > list_of_integers[mid + 1]):
        return peak
    elif peak < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
