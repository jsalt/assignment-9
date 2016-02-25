#!/usr/bin/env python
# encoding: utf-8
"""
created by me for task1 to do 5 different string methods
"""


def method_1(my_string):
    """
    change string to upper case
    """
    return my_string.upper()


def method_2(my_string):
    """
    change string to lower case
    """
    return my_string.casefold()


def method_3(my_string):
    """
    spilit the string
    """
    return my_string.split()


def method_4(my_string):
    """
    find word "is"
    """
    return my_string.find("is")


def method_5(my_string):
    """
    count word "is"
    """
    return my_string.count("is")


def main():
    my_string = input("string")
    A = method_1(my_string)
    print(A)
    B = method_2(my_string)
    print(B)
    C = method_3(my_string)
    print(C)
    D = method_4(my_string)
    print(D)
    E = method_5(my_string)
    print(E)

if __name__ == '__main__':
    main()
