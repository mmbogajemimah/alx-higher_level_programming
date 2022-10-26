#!/usr/bin/python3
''' Finding the peak '''


def find_peak(list_of_integers):
    """ Return a peak in a list of unsorted integers. """
    if len(list_of_integers) == 0:
        return None

    length = len(list_of_integers)
    if length == 1:
        return list_of_integers[0]
    elif length == 2:
        return max(list_of_integers)

    mid = int(length / 2)
    high = list_of_integers[mid]
    if high > list_of_integers[mid - 1] and high > list_of_integers[mid + 1]:
        return high
    elif high < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
