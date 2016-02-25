# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 21:47:08 2016

@author: Marco
"""


examl = str("""
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
""")

def remove_lines(string):
    '''removing extra lines at the end'''
    return string.strip('\n')
    

def tab_2_comma_replacer(string):
    '''replacing tabs by commas'''
    return string.replace('\t', ',')


def line_separator(string):
    '''this creates a list where every item will be an ExaML_info'''
    return string.split('\n\n')
    

def main(string):
    lines = remove_lines(string)
    comma = tab_2_comma_replacer(lines)
    lines_seps = line_separator(comma)
    return lines_seps
    

if __name__ == '__main__':
    new_file = main(examl)
    # this is a for loop to print every item in the list 'new_file' in a separate row    
    for line in new_file:
        print(line)