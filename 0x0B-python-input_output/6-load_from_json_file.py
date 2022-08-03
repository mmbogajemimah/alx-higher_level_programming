#!/usr/bin/python3
"""
task 6 module
"""


import json


def load_from_json_file(filename):
    """
     a function that creates an Object from a “JSON file”
     """
    with open(filename, mode="r", encoding="utf-8") as f:
        object = json.load(f)
    return object
