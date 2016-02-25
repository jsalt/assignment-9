#!/usr/bin/env python
# utf-8


"""
Assignment 9, Task 3
Jon Nations on 24 February 2016

"""


import argparse


def input():
    parser = argparse.ArgumentParser(
           description="""accepts a list of numbers"""
       )
    parser.add_argument(
           '-numbers',
           nargs='+',
           type=int,
           help='Enter list of numbers, no commas'
       )
    args = parser.parse_args()
    return args.numbers
    # accepts user input and sends it  to main


def no_evens(y):
    # removes even numbers
    for i in y:
        if i % 2 == 0:
            y.remove(i)
    return y


def main():
    y = (input())
    odds = no_evens(y)
    print(odds)

if __name__ == '__main__':
    main()
