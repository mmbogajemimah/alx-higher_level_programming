#!/usr/bin/python3
"""
1-my_list module
"""


class MyList(list):
    """
    sorts the list in a class
    """
    def print_sorted(self):
        print(sorted(self))
