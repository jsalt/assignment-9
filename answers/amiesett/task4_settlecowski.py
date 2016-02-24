#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
BIOL7800 Assignment 9 Task 4

Amie Settlecowski
25 Feb. 2016

Edited to answer questions in task 4.

(c) 2016 Brant Faircloth || http://faircloth-lab.org/
All rights reserved.

This code is distributed under a 3-clause BSD license. Please see
LICENSE.txt for more information.

Created on 15 February 2016 16:59 CST (-0600)
"""


def function1(l):
    # my_list is passed to function1 as l, not copied
    # and so the deletion of slice 3:5 from l is not local to this function
    # I assign l to a local variable new_list and delete the same slice
    new_list = l
    del new_list[3:5]
    # printing new_list in function1 shows the expected deletion
    print("new_list in function 1: ", new_list)
    # but my_list in the main loop is not affected


def function2(l):
    # slicing a list just returns the slice
    # unless the returned value is assigned to a variable, as it is to l here
    l = l[1:]
    # printing the reassigned locally in function2 shows the alteration
    print("l in function 2: ", l)


def main():
    my_list = ['a', 'b', 'c', 'd', 'e', 'f']
    print("Here is output from function 1:") # not really because of my edits
    print(my_list)
    function2(my_list)
    print("Here is output from function 2:") # not really because of my edits
    print(my_list)


if __name__ == '__main__':
    main()
