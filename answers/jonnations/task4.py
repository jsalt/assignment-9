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
    del l[3:5]


def function2(l):
    l = l[1:]


def main():
    my_list = ['a', 'b', 'c', 'd', 'e', 'f']
    function1(my_list)
    '''
    function1 works correctly. This command removes the
    objects in the list between place 3 and 5 (non inclusive)
    which takes d & e from the list.
    '''
    print("Here is output from function 1:")
    print(my_list)
    function2(my_list)
    '''
    function2 isn't actually doing anything, regardless of the
    presence of function1. In the function itsself having l = l[1:]
    doesn't make anything happen to my_list. l = l is not a command
    It just prints my_list.That's what is happening when the complete program is running; function1 deletes two of the objects from the list, and the
    worthless function2 just prints the list again.
    
    '''
    print("Here is output from function 2:")
    print(my_list)


if __name__ == '__main__':
    main()
