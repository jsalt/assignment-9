# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 16:01:07 2016

@author: Marco
"""


def string_capitals(string):
    """return string in lower cases"""
    return string.lower()
    

def string_find_substring(string, substring):
    """this function demonstrate the string find method"""
    if substring in string:
        return 'substring '+"'"+str(substring)+"'"+' starting position is #' + str(string.find(substring))
    else:
        return "substring is not in string"


def string_stripper(string, stripper):
    """this function takes out the last character from your string"""
    return string.strip(stripper)
    
    
def string_upper(string):
    "function that convert your string to uppercases"
    return string.upper()
    

def string_replacer(string, replaced, replacer):
    "function that uses the method replace"    
    return string.replace(replaced,replacer)    


def main(string, substring, stripper, replaced, replacer):    
    """
    this main function takes five arguments: the string that will be manipulated,
    a substring that we will check whether or not it is on the inputed string,
    a character to be stripped out at the end of the string, and a couple of
    characters that will be used in the replace method (replaced and replacer).
    """    
    capitals = string_capitals(string)
    print(capitals)
    find_substring=string_find_substring(string, substring)
    print(find_substring)
    stripper = string_stripper(string, stripper)
    print(stripper)
    upper_cases = string_upper(string)
    print(upper_cases)
    repl = string_replacer(string,replaced,replacer)
    print(repl)
    

STRING = "The most beautiful thing we can experience is the mysterious. It is the source of all true art and science."

    
if __name__ == '__main__':
    main(STRING,'beautiful','.','.',',')
    