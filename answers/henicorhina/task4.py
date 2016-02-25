#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
(c) 2016 Brant Faircloth || http://faircloth-lab.org/
All rights reserved.

This code is distributed under a 3-clause BSD license. Please see
LICENSE.txt for more information.

Created on 15 February 2016 16:59 CST (-0600)

BIOL7800 assignment 9
Oscar Johnson 23 February 2016
"""


def function1(l):
    """
    since the variable l is a global variable, the deletion of [3:5]
    affects the variable when it is printed through the main function
    """
    del l[3:5]


def function2(l):
    """
    here, the splice of a global variable l is assigned to a local variable l
    but the global variable remains unaffected
    this can be shown by using the following code:    
    x = l[1:]
    print(x)   
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