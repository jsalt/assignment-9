#!/usr/bin/env python

"""
Task 3:
Here's a list: [1,2,3,4,5,6,7,8,9,10]

Write a program that takes this list (using argparse) as input, and passes the
list to a function. Within the function, use iteration to remove every
even-numbered item from the list, and return only the list containing odd
numbers to the main loop. As always, your program should contain a main loop
and an ifmain statement.

Credit: Dr. Brant's example in Slack
Credit URL: http://stackoverflow.com/questions/11233355/generating-a-list-of-
even-numbers-in-python (User: octopusgrabbus)
Date accessed: Feb 24, 2016

Created by Shraddha Shrestha on February 24, 2016.
Copyright 2016 Shraddha Shrestha. All rights reserved.

 """
import argparse


def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("my_list", type=int, nargs='+', help="use list of\
     integers")
    # without "nargs" this gave error. Importat to run the command multiple
    # times.
    args = parser.parse_args()
    return args.my_list


def get_odd_integers(integers):
    list_1 = []
    for x in integers:
        if x % 2 != 0:
            list_1.append(x)
    return list_1


def main():
    my_list = parser()
    result = get_odd_integers(my_list)
    print(result)


if __name__ == '__main__':
    main()
