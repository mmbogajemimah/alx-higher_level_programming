#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary is {}:
        return "None"
    else:
        maximum = 0
        win = ""

        for key, value in a_dictionary.items():
            if value > maximum:
                maximum = value
                win = key
        return win
