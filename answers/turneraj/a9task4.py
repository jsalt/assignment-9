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
	"""Lists are mutable objects, so the first function directly changes the original
	list found in the main() loop by slicing out items between position 3 and 5
	('d' and 'e').The output is ['a', 'b', 'c', 'f'], which replaces the original
	list globally. When the list is printed in the main() loop, the new, modified list
	is given.""" 
	del l[3:5]
	
	
	
def function2(l):
	"""When the list 'l' is called into the second function, it is passed the edited
	list 'l' from function1(). Although you would expect an output of ['b', 'c', 'f'],
	the output value is the modified list from function 1. This is because you do not include a
	return statement that will give the expected output when l and function 2 are called in the
	main loop. By using "return l" in function2 and "l = function2(my_list) in the main() loop,
	you will get the desired outcome."""
	l = l[1:]
	

def main():
	my_list = ['a', 'b', 'c', 'd', 'e', 'f']
	function1(my_list)
	print("Here is output from function 1:")
	print(my_list)
	function2(my_list)
	print("Here is output from function 2:")
	print(my_list) #simply gives the modified list from function1


if __name__ == '__main__':
    main()