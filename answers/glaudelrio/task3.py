#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 21:42:02 2016

@author: Glaucia
"""
"""

Task 3

Here's a list: [1,2,3,4,5,6,7,8,9,10]

Write a program that takes this list (using argparse) as input, 
and passes the list to a function. Within the function, use iteration 
to remove every even-numbered item from the list, and return only the list 
containing odd numbers to the main loop. As always, your program should contain a 
main loop and an ifmain statement.

"""
import argparse

def listinput():
    """asks for the input list and passes it to the function, the list must be typed afetr --my_list
    Example: my_list 1 2 3 4 5 6 7 8"""
    parser = argparse.ArgumentParser()
    #this is going to tell the user to add the my list argument in the comand prompt
    parser.add_argument("--my_list", dest="my_list",required=True, nargs="+", type=int,
                        help="a list of numbers is required, like 1 2 3 4 5 6")   
    args=parser.parse_args()   
    result=Justodd(args.my_list)
    #returns the result of Justodd with the given input    
    return result


def Justodd(my_list):
    """gets all the values in a list and resturns only the odd values inside another list"""
    #setting an empty list to store my results"""    
    resultlist=[]
    #iteration to deal with all the numbers provided in the input    
    for number in my_list:
        #tests if number modulos is different from 0, or if the number is odd
        if number%2 != 0:
            #if it is odd append to a list
           resultlist.append(number) 
        else:
           pass 
    #returns the result in a list
    return resultlist


def main():
    #stores the result list in a variable
    list_of_numbers = listinput()
    #prints that variable
    print(list_of_numbers)
    
    
if __name__ == "__main__":
    main()


    
