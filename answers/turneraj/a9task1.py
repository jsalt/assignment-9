#!/usr/bin/env python
# encoding: utf-8

"""
 My first task for Assignment 9 that creates five different functions to use built in attributes on a string.

 Created by A.J. Turner on February 23, 2016
 Copyright 2016 A.J. Turner. All rights reserved.

"""

def allcaps(mystring):
	upper = mystring.upper() #capitalizes all letters in string
	print("Method 1 example:", upper, "\n")


def locate(mystring):
	where = mystring.find("mysterious")
	print("Method 2 example: The location of 'mysterious' is ", where, "\n")


def low(mystring):
	firstlet = mystring.lower() #all letters made lowercase
	print("Method 3 example:", firstlet, "\n")


def titlecase(mystring):
	mytitle = mystring.title() #makes string titlecase, capitalizing first letter of each word
	print("Method 4 example:", mytitle, "\n")


def swapit(mystring):
	myswap = mystring.swapcase() #swaps lowercase and uppercase letters
	print("Method 5 example:", myswap, "\n")


def main():
	#string used in all functions above
	mystring = "The most beautiful thing we can experience is the mysterious. It is the source of all true art and science."
	
	allcaps(mystring) #first example
	
	locate(mystring)#second example
	
	low(mystring)#third example
	
	titlecase(mystring)#fourth example
	
	swapit(mystring)#fifth example


if __name__ == '__main__':
    main()