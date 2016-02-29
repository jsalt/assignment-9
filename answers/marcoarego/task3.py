# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 22:20:06 2016

@author: Marco
"""
# importing modules
import argparse
#lista = [1,2,3,4,5,6,7,8,9,10]

def get_even_numbers(lista):
    '''function to get the odd numbers of a list of integers'''
    odds = []
    for number in lista:
        # testing if the remainder of a division by 2 is equal to zero
        if number % 2 == 0:
            pass
        else:
            odds.append(number)
    return odds
    
    
def parser_function():
    parser = argparse.ArgumentParser(description="""my argument parser""")
    # Adding an argument to 'parse'    
    parser.add_argument('-l','--my_list', dest = "lista", nargs='+', 
                        required=True, type=int, 
                        help='please insert -l followed by the integers values'
                        ' you want for this list. The numbers should be enter'
                        ' like this: 1 2 3 4 5...')
    args = parser.parse_args()
    result = get_even_numbers(args.lista)
    return result


def main():
    result = parser_function()
    print(result)    
    return result


if __name__ == '__main__':
    main()
    
