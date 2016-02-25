# !/usr/bin/env python
# encoding: utf-8


"""
created by me for task3 to remove every even-numbered item from the list
"""

import argparse


def parser():
    """
   using argparse to takes the list  as input
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("integers",
                        help=" Enter integers:",
                        type=int,
                        nargs="+",
                        )
    args = parser.parse_args()
    return args.integers


def remove_even(l):
    for i in l:
        if i % 2 == 0:
            l.remove(i)
    return l


def main():
    result1 = remove_even(parser())
    print(result1)


if __name__ == '__main__':
    main()
