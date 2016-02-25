#! /usr/bin/env python
# encoding UTF-8

"""
Assignment8Task1 biol7800
ZacCarver 02/25/2016
'''
(c) 2016 Brant Faircloth || http://faircloth-lab.org/
All rights reserved.

This code is distributed under a 3-clause BSD license. Please see
LICENSE.txt for more information.

Created on 15 February 2016 16:59 CST (-0600)
'''
"""


def function1(l):
    '''Once the list from main() is passed to this fxn it is modified and is \
    and where l is globally set and is modified to exclude elements between \
    indecies 3 and 5'''
    del l[3:5]


def function2(l):
    '''Each item from 'my_list' is captured, yet 'l' here is not relayed back \
    to main()--keeping its local value.'''
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
