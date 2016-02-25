#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
(c) 2016 Brant Faircloth || http://faircloth-lab.org/
All rights reserved.

This code is distributed under a 3-clause BSD license. Please see
LICENSE.txt for more information.

Created on 15 February 2016 16:59 CST (-0600)
"""


def function1(l):
    """
    items 3 and 4 from the list are deleted by this function. Because
    1 is not assign to anything , it is global variable and can change my_list
    """
    del l[3:5]


def function2(l):
    """
    In this function, 1 is assigned as a local variable under the body of
    function2. we should return or print this local variable in main function
    to see the modification (capture all items except the first one)

    """
    l = l[1:]


def main():
    my_list = ['a', 'b', 'c', 'd', 'e', 'f']
    function1(my_list)
    print("Here is output from function 1:")
    print(my_list)
    function2(my_list)
    print("Here is output from function 2:")
    print(my_list)


if __name__ == '__main__':
    main()
