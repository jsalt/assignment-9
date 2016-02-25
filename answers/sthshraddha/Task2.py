#!/usr/bin/env python

"""
Task 2:
Here are some data from ExaML - a phylogenetic inference program - represented
as a string. In this case, these data are from different runs of the program,
and they indicate the log-likelihood scores for a set of trees inferred by the
program. The data are tabular in format, more specifically, they are
tab-delimited. Write a program that processess these data to split them by line
ending, replaces the tab separations with commas, and prints out the result -
line-by-line. As always, your program should contain a main loop and an
ifmain statement.

Credit URL: http://ianrolfe.livejournal.com/37398.html
Date accessed: Feb 24, 2016

Created by Shraddha Shrestha on February 24, 2016.
Copyright 2016 Shraddha Shrestha. All rights reserved.

 """
import re


def remove_empty_lines():
    data = """ExaML_info.T6\tLikelihood of best tree:\t-82924194.67\n
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
            """
    # The following command replaces tab with comma. 
    replace_tab = data.replace("\t", ",")
    # Using regular expressions to replace empty lines
    return re.sub("\n\s*\n*", "\n", replace_tab)


def main():
    result = remove_empty_lines()
    print(result)

if __name__ == '__main__':
    main()
