#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 21:06:39 2016

@author: Glaucia
"""

"""
Task 1

Here is a quote from Albert Einstein:

"The most beautiful thing we can experience is the mysterious. 
It is the source of all true art and science."
This quote is also a string. Write a program that 
includes 5 different functions each of which demonstrates one of 
5 different string methods. As always, your program should contain a main loop and an ifmain statement.

"""
def uppercase():
    """this function transforms all the letters in this string in capital letters 
    and prints the resulting string"""
    mystring =str("The most beautiful thing we can experience is the mysterious." 
                  "It is the source of all true art and science.")
    result=mystring.upper()
    print(result)


def lowercase():
    """this function transforms all the letters in this string in lower 
    case letters and prints the resulting string"""
    mystring = str("The most beautiful thing we can experience is the mysterious." 
                  "It is the source of all true art and science.")    
    result=mystring.lower()
    print(result)


def replaceEs():
    """this function replaces lower case "e" by capital E"" and prints the resulting string"""
    mystring = str("The most beautiful thing we can experience is the mysterious." 
                  "It is the source of all true art and science.")  
    result=mystring.replace("e", "E")
    print(result)


def periodaspartition():
    """prints a tuple containing the left part of the string split by the separator ".", 
    the separator itself and the right part of the string."""
    mystring = str("The most beautiful thing we can experience is the mysterious." 
                  "It is the source of all true art and science.")   
    result=mystring.partition(".")
    print(result)


def eachword():
    """prints a list with every word in the string as a different element in the list"""
    mystring = str("The most beautiful thing we can experience is the mysterious." 
                  "It is the source of all true art and science.")   
    result=mystring.split()
    print(result)


def main():
    uppercase()
    lowercase()
    replaceEs()
    periodaspartition()
    eachword()
  
  
if __name__ == "__main__":
    main()
   
    
