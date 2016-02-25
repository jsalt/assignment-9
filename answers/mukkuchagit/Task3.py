#!/usr/bin/env python
# encoding: utf-8
"""
strings and list assignment.

Copyright 2016 Mukesh Maharjan. All rights reserved.
"""
import argparse


def paser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--list_of_integers', nargs='+', help="enter a list of \
    integers", type=int)
    args = parser.parse_args()
    return args.list_of_integers


def onlyodd(my_list):
    for i in my_list:
        if i % 2 == 0:
            my_list.remove(i)
            return my_list


def main():
    my_list = paser()
    print(onlyodd(my_list))

if __name__ == '__main__':
    main()
