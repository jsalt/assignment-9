#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
(c) 2016 Brant Faircloth || http://faircloth-lab.org/
All rights reserved.

This code is distributed under a 3-clause BSD license. Please see
LICENSE.txt for more information.

Created on 15 February 2016 16:59 CST (-0600)

Function comments added by Andre Moncrieff on 23 Feb 2016
"""


def function1(l):
    """
    This function deletes the 3rd and 4th index item from the list. This
    deletion is of global consequence. For this reason function1 can alter
    my_list in the main loop even when the result from function1 is not sent
    to the main loop explicity.
    """
    del l[3:5]


def function2(l):
    """
    This function captures all items in the input list except the first.
    This modification is not of global consequence, unlike the deletion of
    function1. For function2's modification to be evidenced in a print
    statement, the output would first need to be explicitly returned to the
    main loop and then printed.
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
