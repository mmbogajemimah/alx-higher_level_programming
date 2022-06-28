#!/usr/bin/python3
def uppercase(str):
    new_string =""
    for i in range(len(str)):
        if (ord(str[i]) >= 97 and ord(str[i]) <= 122):
            new_string = new_string + chr((ord(str[i]) - 32))
            continue
        else:
            new_string = new_string + str[i]
    print("{0}".format(new_string));
