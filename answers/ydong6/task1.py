#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Feb 24, 2016
Here is a quote from Albert Einstein:

"The most beautiful thing we can experience is the mysterious. It is the source of all true art and science."
This quote is also a string. Write a program that includes 5 different functions
each of which demonstrates one of 5 different string methods. As always, your
program should contain a main loop and an ifmain statement. 

@author: Yuankai Dong
'''


def function1():
    mystring='The most beautiful thing we can experience is the mysterious. \nIt is the source of all true art and science.'
    new_string = mystring.upper()
    print("function1=" ,new_string)
    
    
def function2(): 
    mystring='The most beautiful thing we can experience is the mysterious. \n It is the source of all true art and science.'
    second_string=mystring.split(" ")
    print("function2=",second_string)
    
    
def function3():
    mystring='The most beautiful thing we can experience is the mysterious. \n It is the source of all true art and science.'
    c=mystring.count('m')
    print("function3=",c)
    

def function4():
    mystring='The most beautiful thing we can experience is the mysterious. \n It is the source of all true art and science.'
    d=mystring.find('mysterious')
    print("function4=", d)
    
    
def function5():
    mystring='The Most beautiful thing we can Experience is the mysterious.  \nIt is the source of all true art and science.'
    e=mystring.lower()
    print("function5=",e)



def main():
    function1()
    function2()
    function3()
    function4()
    function5()
    
    
if __name__ == '__main__':
    main()