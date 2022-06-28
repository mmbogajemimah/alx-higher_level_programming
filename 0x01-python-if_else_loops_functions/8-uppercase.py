#!/usr/bin/python3
def uppercase(str):
    new_string =""
    for i in range(len(str)):
        if str[i] >= 'a' and str[i] <= 'z':
            new_string = new_string + chr((ord(str[i]) - 32))
        else:
            new_string = new_string + str[i]
    print("{}".format(new_string));
