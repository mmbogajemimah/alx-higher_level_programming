#!/usr/bin/python3

import sys

if __name__ == "__main__":

    length = len(sys.argv)
    print(length)
    sum = 0
    
    for i in range(1, length):
        sum += int(sys.argv[i])
    print(sum)
