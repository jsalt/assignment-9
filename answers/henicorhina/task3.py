# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
BIOL7800 assignment 9
Oscar Johnson 23 February 2016
"""

import argparse


def get_args():
    parser = argparse.ArgumentParser(
            description="""takes a list of integers and removes the even numbers"""
        )
    parser.add_argument('--list',
                        dest = "list",
                        required = True,
                        nargs = '+',
                        type = int,
                        help = "enter a list of integers to remove the even numbers"
                        )
    return parser.parse_args()


def remove_even(args):
    """
    removes the even numbers from a list and returns the list
    """
    evens = args.list[1::2]
    return evens


def main():
    args = get_args()
    x = (remove_even(args))
    print(x)

if __name__ == '__main__':
    main()