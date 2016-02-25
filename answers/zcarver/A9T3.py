#! /usr/bin/env python
# encoding UTF-8

'''
Assignment9Task3 biol7800
ZacCarver 02/25/2016
Task3-list: [1,2,3,4,5,6,7,8,9,10]

Write a program that takes this list (using argparse) as input, and passes \
the list to a function. Within the function, use iteration to remove every \
even-numbered item from the list, and return only the list containing odd \
numbers to the main loop.
'''

import argparse


def psr():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ls_o_ints', nargs='+', help="enter a list of \
    integers", type=int)
    args = parser.parse_args()
    return args.ls_o_ints


def remevn(ls):
    for i in ls:
        if i % 2 == 0:
            ls.remove(i)
            return ls


def main():
    ls = psr()
    print(remevn(ls))

if __name__ == '__main__':
    main()
