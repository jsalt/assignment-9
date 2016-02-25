#!/usr/bin/env python
# encoding: utf-8
"""
strings and list assignment.

Copyright 2016 Mukesh Maharjan. All rights reserved.
"""


def function1(l):
    del l[3:5]
    '''here we are deleting the items in the list ['a','b','c','d','e','f']
     from 3 to 5 (which is 'd' and 'e'),
     hence the output is: ['a','b','c','f']'''


def function2(l):
    l = l[1:]
    '''From function1, we altered the list to['a', 'b', 'c', 'f'].
    Hence the output of fucntion2 should have been ['b', 'c', 'f'],
    instead we get the back input list unmodified because, the input value is
    not yet changed by the assignment of new value so it simply returns
    the input value again, which is ['a','b','c','f'].'''


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
