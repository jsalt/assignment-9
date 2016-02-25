#! /usr/bin/env python
# encoding: utf-8

'''
Grace Cagle
22 Feb 2016
Assignment 9 Task 3
Argparse code modified from Brant Faircloth
'''


import argparse


def get_args():
    parser = argparse.ArgumentParser(
            description="""my argument parser""")
    parser.add_argument(
            "--my_list",
            required=True,
            nargs='+',
            type=int,
            help="""The list you want to enter"""
        )
    return parser.parse_args()


def odd_num(n=1):
    '''remove even numbers using iteration and
    pass a list of odd numbers to the main loop'
    This function does not work :( '''
    args = get_args()
    num_list = args.my_list
    if n > 10:
        return
    else:
        del num_list[n]
        n += 2
        odd_num(n)



def main():
    # args = get_args()
    # print(args.my_list)
    print(odd_num(n=1))

if __name__ == '__main__':
    main()
