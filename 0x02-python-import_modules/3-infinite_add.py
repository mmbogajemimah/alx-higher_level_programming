#!/usr/bin/python3
import sys

if __name__ == '__main__':
    args = sys.argv
    l_args = len(args)
    sum = 0

    if l_args > 1:
        for i in range(1, l_args):
            sum += int(args[i])

    print(sum)
