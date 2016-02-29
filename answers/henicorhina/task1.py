# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
BIOL7800 assignment 9
Oscar Johnson 23 February 2016
"""


def count(string):
    """
    counts all instances of the letter 'a' in a string
    """
    x = string.count("a")
    return x


def upper(string):
    """
    makes all characters upper case
    """
    x = string.upper()
    return x


def lower(string):
    """
    makes all characters lower case
    """
    x = string.lower()
    return x


def split(string):
    """
    splits a string into a list
    delimited by spaces
    """
    x = string.split()
    return x


def find(string):
    """
    finds science
    in a string
    returns the index value
    """
    x = string.find("science")
    return x


def main():
    my_string = "The most beautiful thing we can experience is the mysterious. It is the source of all true art and science."
    u = count(my_string)    
    v = upper(my_string)
    x = lower(my_string)
    y = split(my_string)
    z = find(my_string)
    print("count of 'a' in my string: ", u, "\n", 
          "my string, in upper case: ", v, "\n", 
          "my string, in lower case: ", x, "\n", 
          "string split to a list: ", y, "\n", 
          "find the science! ", z)

if __name__ == '__main__':
    main()