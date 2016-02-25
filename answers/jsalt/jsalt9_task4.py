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
    '''Here we use the `del` function with the slice operator to permanently\n
    remove the the items within 3rd and 5th partiitions\n
    (in this case 'd' and 'e') from the original list. This works because\n
    lists are mutable, so we are actually modifying the contents of the\n
    original list. So although we have not returned a value, when we print\n
    my_list from the main function, we are printing the new, altered list.'''
    del l[3:5]


def function2(l):
    '''Because we altered my_list with function1, the input here is actually\n
    ['a', 'b', 'c', 'f'] (see above). However, although we might expect the\n
    print statement to produce ['b', 'c', 'f'], instead we get the back the\n
    input list. This is because here the slice operator creates a new list,\n
    which we assign to l, but we have not actually modified the original\n
    caller list. Thus, when we go to print function2(my_list), we get the\n
    input value back.'''
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
