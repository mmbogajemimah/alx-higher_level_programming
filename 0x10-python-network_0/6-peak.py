#!/bin/bash
def quicksort(l):
    arr = l[::]
    if len(arr) <= 1:
        return arr
    l = [x for x in arr[1:] if x <= arr[0]]
    r = [x for x in arr[1:] if x > arr[0]]
    return quicksort(l) + arr[0:1] + quicksort(r)


def find_peak(list_of_integers):
    if len(list_of_integers) <= 0:
        return None
    array = quicksort(list_of_integers)
    return array[-1]
