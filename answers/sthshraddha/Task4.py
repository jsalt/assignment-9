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
    # This is deleting items in my_list from index 3 to index 4. Item in index
    # 5 is not deleted.
    del l[3:5]


def function2(l):
    # When def function(l) is not executed, then function2(my_list) gives the
    # correct output, which is ['a', 'b', 'c', 'd', 'e', 'f']. But when
    # function1(l) is run, then it gives the wrong output:['a', 'b', 'c', 'f'].
    # This is probably because since there is no loop, no return, after
    # function1(my_list) runs, the list it prints (['a', 'b', 'c', 'f']) is the
    # input list for function2(my_list). So function2(my_list) is running but
    # the list for function2 is ['a', 'b', 'c', 'f'].
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
