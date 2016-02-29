#!/usr/bin/env python
# encoding: utf-8

"""
 My third task for Assignment 9 that uses argparse within a program that uses iteration over a list to remove even numbers and only print out odd numbers. Orginal argparse function modified from Brant C. Faircloth. 

 Created by A.J. Turner on February 24, 2016
 Copyright 2016 A.J. Turner. All rights reserved.

"""
import argparse


def my_args():
    parser = argparse.ArgumentParser(
            description="""argument parser to remove even integers from list""")
    parser.add_argument(
            "--my_list",
            required=True,
            nargs='+',
            type=int,
            help="""The list of integers you want to enter"""
        )
    return parser.parse_args()


def toss_evens(noeven):
	for num in noeven:
		if num %2 == 0: #specifies even numbers in list
			noeven.remove(num) #removes even numbers
	return noeven #gives odd numbers since evens were removed
	

def main():
	args = my_args()
	print(toss_evens(args.my_list))

  
if __name__ == '__main__':
    main()