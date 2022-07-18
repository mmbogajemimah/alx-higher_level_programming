#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if value >= 0 or value < 0:
            print("{:d}".format(value))
            is_digit = True
    except Exception:
        is_digit = False
    return is_digit
