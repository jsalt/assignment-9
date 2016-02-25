#!/usr/bin/env python
# encoding: utf-8

"""
BIOL7800 Assignment 9 Task 3

Amie Settlecowski
25 Feb. 2016

This program inputs a list via argparse and parses out even numbers.
"""
import argparse


def input_list():
    # parses user input and returns phrase to main
    # source: https://youtu.be/rnatu3xxVQE
    parser = argparse.ArgumentParser()
    parser.add_argument("--list",
                        required=True,
                        nargs='+',
                        type=int,
                        help="Enter a list of intergers separated by spaces")
    args = parser.parse_args()
    return args.list


def odd_even(x):
    # takes integer x and returns 0 when x is 0 or even and 1 when x is odd
    return x % 2


def remove_even(l):
    count = 0
    for n in l:
        if odd_even(n) == 0:
            l.pop(count)
        else:
            pass
        count += 1
    return l


def main():
    l = input_list()
    l_odd = remove_even(l)
    print(l_odd)

if __name__ == '__main__':
    main()
