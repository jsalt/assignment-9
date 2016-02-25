#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Assignment 9
Task 1 Program: String methods
Jessie Salter
23 February 2016
"""


def string_split(quote):
    '''Produces a list of words based on spaces in the original string'''
    return quote.split()


def string_islower(quote):
    '''Determines whether the string is all lowercase'''
    return quote.islower()


def string_lower(quote):
    '''Lowercases the string'''
    return quote.lower()


def string_partition(quote):
    '''Partitions the string after the first period and produces a tuple with \n
    both sentences and the period'''
    return quote.partition('.')


def string_replace(quote):
    '''Replaces 'beautiful' with 'abhorrent', returns a copy of the string'''
    return quote.replace('beautiful', 'abhorrent')


def main():
    quote = "The most beautiful thing we can experience is the mysterious. It is the source of all true art and science."
    print(string_split(quote))
    print(string_islower(quote))
    print(string_lower(quote))
    print(string_partition(quote))
    print(string_replace(quote))


if __name__ == '__main__':
    main()
