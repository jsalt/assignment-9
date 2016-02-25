#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 22:01:01 2016

@author: Glaucia
"""
"""
Task 4

In the following program, we are performing some operations on a list, 
but we never return the list to the main() loop. However, when we print() 
the list within the main function after running function1, it appears to have been 
modified. Then, after running function2, the list does not appear to be modified further. 
Why do you see these different behaviors between function1 and function2? Answer the question 
for each function by copying the code below to task5.py within your github username 
directory and adding your explanation to each function as a function description.

"""

"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
"""
(c) 2016 Brant Faircloth || http://faircloth-lab.org/
All rights reserved.

This code is distributed under a 3-clause BSD license. Please see
LICENSE.txt for more information.

Created on 15 February 2016 16:59 CST (-0600)
"""


def function1(l):
    """this function is basically deleting the values corresponding to 3 (inclusive) 
    to 5 (not inclusive in the list), since del is an operator, the function modifies 
    my_list without the need of a return statement. del is useful when you don't need the removed value 
    anymore. Lists are mutable, and then we have to be careful with the use of operators such as del"""
    del l[3:5]


def function2(l):
    """this function is basically calling all the elements in the list from the first one to the last,
    but it is not returning the value. So my_list is not modified by this function, it is just stored
    in this l variable inside the function. This way, my_list keeps being the same ['a', 'b', 'c', 'f'] 
    generated after the use of the operator del in the first function"""
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