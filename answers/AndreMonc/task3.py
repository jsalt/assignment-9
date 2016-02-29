# !/usr/bin/env python
# encoding: utf-8


"""
My list program
Created by Andre Moncrieff on 23 Feb 2016.
Copyright 2016 Andre E. Moncrieff. All rights reserved.
"""

import argparse


def parser():
    """
    Create argument input
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("list_of_integers", nargs="+", type=int,
                        help=("Please input a list of integers. Example: " +
                              "1 2 3 4 5 . . ."))
    args = parser.parse_args()
    return args.list_of_integers


def only_odds(input):
    list_of_odds = []
    for item in input:
        if item % 2 != 0:
            list_of_odds.append(item)
    return list_of_odds


def main():
    odds = only_odds(parser())
    print(odds)


if __name__ == '__main__':
    main()
