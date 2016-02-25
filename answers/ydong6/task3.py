
#!/usr/bin/env python
# encoding: utf-8
'''
Created on Feb 25, 2016
Here's a list: [1,2,3,4,5,6,7,8,9,10]

Write a program that takes this list (using argparse) as input, and passes the
list to a function. Within the function, use iteration to remove every even-
numbered item from the list, and return only the list containing odd numbers to
the main loop. As always, your program should contain a main loop and an ifmain
statement.
@author: Yuankai Dong
'''

    
import argparse   


def parser(): 
    parser = argparse.ArgumentParser()
    
    # Adding an argument to 'parse'
    parser.add_argument("list",
                       help= "Please input the list" 
                       " after the function name" ,
                       type=list)
    #parser.add_argument("-o","--output", help="output result to a file\n",
     #                   action="store_true")
                            
    args = parser.parse_args()
    return args.list


def function1(list=parser()):
    list = [1,2,3,4,5,6,7,8,9,10]
    i = 0
    while i < 10:
        for i in list:
            if i % 2 == 0:
                list.remove(i)
        print(list)     
    

def main(): 
    function1()
    
   
if __name__ == '__main__':
    main()