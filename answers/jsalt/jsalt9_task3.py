#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Assignment 9
Task 3 Program: Extracting odd numbers from a list
Jessie Salter
23 February 2016
"""

import argparse


def prompt():
    '''This function takes user input'''
    parser = argparse.ArgumentParser(
        description='''Takes integers and puts them into a list''')
    parser.add_argument(
        "-intlist",
        # Must have a flag or will be treated as input value
        help="Enter a list of integers",
        nargs='+',
        type=int)
    args = parser.parse_args()
    return args.intlist


def odds(my_list):
    '''Removes even integers from a given list'''
    for num in my_list:
        if num % 2 == 0:
            # This will catch even numbers
            my_list.remove(num)
            # This will remove even numbers from the list
    return my_list


def main():
    my_list = prompt()
    print(odds(my_list))


if __name__ == '__main__':
    main()
