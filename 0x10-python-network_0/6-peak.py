#!/usr/bin/python3
''' Finding the peak '''


def find_peak(list_of_integers):
    if len(list_of_integers) <= 0:
        return None
    array = sorted(list_of_integers)
    return array[-1]
