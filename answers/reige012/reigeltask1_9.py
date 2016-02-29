#!/usr/bin/env python
# encoding: utf-8

"""
This program demonstrates 5 different string methods.

Edited by Alicia Reigel. 24 February 2016.
Copyright Alicia Reigel. Louisiana State University. 24 February 2016. All
rights reserved.

"""


def uppercasing_strings():
    # this function makes each letter in the string uppercase
    string = ("""The most beautiful thing we can experience is the mysterious."""
    """It is the source of all true art and science.""")
    return string.upper()


def stripping_strings():
    # this function strips the period off the end of the string
    string = ("""The most beautiful thing we can experience is the mysterious."""
    """It is the source of all true art and science.""")
    return string.strip('.')


def counting_strings():
    # this function counts all of the "e" letters in the string
    string = ("""The most beautiful thing we can experience is the mysterious."""
    """It is the source of all true art and science.""")
    return string.count('e')


def splitting_strings():
    # this function splits the string into individual words in list format
    string = ("""The most beautiful thing we can experience is the mysterious."""
    """It is the source of all true art and science.""")
    return string.split(' ')


def swappingcases_strings():
    # this function swaps the case of each letter from upper to lower and vice versa
    string = ("""The most beautiful thing we can experience is the mysterious."""
    """It is the source of all true art and science.""")
    return string.swapcase()


def main():
    print(uppercasing_strings())
    print(stripping_strings())
    print(counting_strings())
    print(splitting_strings())
    print(swappingcases_strings())


if __name__ == '__main__':
    main()
