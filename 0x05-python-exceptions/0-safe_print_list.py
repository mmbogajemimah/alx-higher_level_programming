#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for item in my_list:
        count = count + 1
    try:
        if x <= count:
            for i in range(x):
                print("{:d}".format(my_list[i]), end="")
            print()
            return x
        else:
            for i in range(count):
                print("{:d}".format(my_list[i]), end="")
            print()
            return count
    except IndexError:
        print("Index Error")
