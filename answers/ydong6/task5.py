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
    '''List is mutable. This function changed the my_list by using del. del can
perform to the main function. therefore the result changed.'''
    del l[3:5]


def function2(l): 
    '''This function actually changed the list that has been input to this function. 
    However, it only changes inside the function. 
    It put the changed list to a variable named l. The result did not come back to my_list. 
    so when we print the my_list from main function, it appears not change.
    '''
    l = l[1:]
    #print(l)


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