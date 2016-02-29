#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This code is edited by Alicia Reigel on 25 February 2016 to place in function
descriptions for both function1 and function2.
Original:
(c) 2016 Brant Faircloth || http://faircloth-lab.org/
All rights reserved.
This code is distributed under a 3-clause BSD license. Please see
LICENSE.txt for more information.
Created on 15 February 2016 16:59 CST (-0600)

"""


def function1(l):
    """This function deletes values between 3 and 5 index spaces which are "d"
    and "e. The del function removes items from the list based on its index
    location. The del function is created as a recurvsive function that
    actively works on the list altering the original as it works. This is why
    without using the return function we can print the list that has been
    permanently altered.
    Source: https://docs.python.org/2/tutorial/datastructures.html"""
    del l[3:5]


def function2(l):
    """Because our first function permanently altered my_list to read
    ["a", "b", "c", "f"], when we run function2 on that new list we expect
    to get back ["b", "c", "f"] but that doesn't happen. Instead the slice
    operator we use here creates a new list called l but it doesn't permanently
    alter the list and therefore since we never return l to the main loop to
    before printing all we are doing is printing our altered my_list from our
    first function. Had we returned l and then printed it we would have seen
    this function working as we expected."""
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
