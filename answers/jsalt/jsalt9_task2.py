#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Assignment 9
Task 2 Program: Processing tab-delimited data
Jessie Salter
23 February 2016
"""


def tab_to_comma(my_data):
    '''Replaces tab separations with commas'''
    return my_data.replace('\t', ',')


def data_split(my_data):
    '''Splits your data file by line ending, creates a list with each line as\n
    a string'''
    my_data = my_data.splitlines()
    # This splits the string up by line into a list
    my_data = list(filter(None, my_data))
    # This removes empty strings created by extra line breaks from the list
    return my_data


def data_print(my_data):
    '''Prints your newly formatted data file out line-by-line'''
    for line in my_data:
        print(line)


def main():
    data = '''
ExaML_info.T6\tLikelihood of best tree:\t-82924194.67\n
ExaML_info.T5\tLikelihood of best tree:\t-82924194.71\n
ExaML_info.T9\tLikelihood of best tree:\t-82924194.73\n
ExaML_info.T7\tLikelihood of best tree:\t-82924252.98\n
ExaML_info.T2\tLikelihood of best tree:\t-82924253.01\n
ExaML_info.T1\tLikelihood of best tree:\t-82924354.95\n
ExaML_info.T8\tLikelihood of best tree:\t-82924354.98\n
ExaML_info.T15\tLikelihood of best tree:\t-82924366.58\n
ExaML_info.T0\tLikelihood of best tree:\t-82924366.59\n
ExaML_info.T4\tLikelihood of best tree:\t-82924397.48\n
ExaML_info.T16\tLikelihood of best tree:\t-82924424.87\n
ExaML_info.T3\tLikelihood of best tree:\t-82924424.89\n
ExaML_info.T14\tLikelihood of best tree:\t-82924426.52\n
ExaML_info.T12\tLikelihood of best tree:\t-82924426.53\n
ExaML_info.T13\tLikelihood of best tree:\t-82924426.54\n
ExaML_info.T19\tLikelihood of best tree:\t-82924465.57\n
ExaML_info.T17\tLikelihood of best tree:\t-82924707.69\n
ExaML_info.T10\tLikelihood of best tree:\t-82925366.65\n
ExaML_info.T18\tLikelihood of best tree:\t-82925393.89\n
ExaML_info.T11\tLikelihood of best tree:\t-82925447.6\n
'''
    step1 = tab_to_comma(data)
    # This captures the list with commas and passes it to the next function
    step2 = data_split(step1)
    # This captures the listified-string and passes it to the print function
    data_print(step2)
    # The function includes the print statement, so we just need to run it

if __name__ == '__main__':
    main()
