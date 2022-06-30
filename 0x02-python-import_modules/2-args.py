#!/usr/bin/python3
import sys

if __name__ == '__main__':    
    n = sys.argv
    length = len(n) - 1

    if length > 1:
        print(length, 'arguments:')
        for i in range(1, length + 1):
            print('{:d}: {}'.format(i, n[i]))
    elif length == 1:
        print(length, 'argument:')
        for i in range(1, length + 1):
            print('{:d}: {}'.format(i, n[i]))
    elif length == 0:
        print(length, 'arguments.')
