#!/usr/bin/env python
# #encoding: utf-8

"""
Program to take a list as input and uses iteration to remove even numbers from
the list.

Created by Alicia Reigel. 24 February 2016.
Copyright Alicia Reigel. Louisiana State University. 24 February 2016.

"""


import argparse


def arg_input():
    # the function parses the user input and sends it back to main loop
    parser = argparse.ArgumentParser(
            description="""takes a list of numbers as input"""
        )
    parser.add_argument(
            '-list_of_numbers',
            nargs='+',
            type=int,
            help='Enter the list'
        )
    args = parser.parse_args()
    return args.list_of_numbers
    # above statement takes the user input and returns it to the main loop.


def evens_out(y):
    # this function uses iteration to find even numbers & remove them
    for i in y:
        if i % 2 == 0:
            y.remove(i)
    return y


def main():
    y = (arg_input())
    final = evens_out(y)
    print(final)

if __name__ == '__main__':
    main()
