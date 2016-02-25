#!/usr/bin/env python
# encoding: utf-8

"""
BIOL7800 Assignment 9 Task 2

Amie Settlecowski
25 Feb. 2016

This program processes and prints ExaML tree log likelihood data.

*** You may need to cd to the directory where  ***
*** this is saved in order to run this program ***
"""


def list_by_line(file_as_string):
    # create a list delimited by newlines from string of 1+ lines
    file_by_line = file_as_string.split('\\n\n')
    return file_by_line


def process_line(line):
    # convert tabs to commas in a string
    edited_line = line.replace("\\t", ",")
    return edited_line


def main():
    with open("task2.txt", 'r') as ifile:
        # check that task2.txt opens in read mode w/out error
        if ifile.readable() == 'False':
            ifile.close()
        else:
            pass

        # read in task_2.txt as one long string
        file_as_string = ifile.read()

        # file_by_line is a list of every line of the file as a string
        file_by_line = list_by_line(file_as_string)

        # iterate over file_by_line to process and print each line in the file
        for line in file_by_line:
            edited_line = (process_line(line))
            print(edited_line)

        ifile.close()

if __name__ == '__main__':
    main()
