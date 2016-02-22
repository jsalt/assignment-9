
## Task 1

Here is a quote from Albert Einstein:
```
"The most beautiful thing we can experience is the mysterious. It is the source of all true art and science."
```

This quote is also a string.  Write a program that includes 5 different functions each of which demonstrates one of 5 **different** string methods. As always, your program should contain a `main` loop and an `ifmain` statement.


## Task 2

Here are some data from ExaML -  a phylogenetic inference program - represented as a string.  In this case, these data are from different runs of the program, and they indicate the log-likelihood scores for a set of trees inferred by the program.  The data are tabular in format, more specifically, they are tab-delimited:

```

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

```

Write a program that processess these data to split them by line ending, replaces the tab separations with commas, and prints out the result - line-by-line. As always, your program should contain a `main` loop and an `ifmain` statement.


## Task 3

Here's a list: `[1,2,3,4,5,6,7,8,9,10]`

Write a program that takes this list (using argparse) as input, and passes the list to a function.  Within the function, use iteration to remove every even-numbered item from the list, and return only the list containing odd numbers to the `main` loop.  As always, your program should contain a `main` loop and an `ifmain` statement.


## Task 4

In the following program, we are performing some operations on a list, but we never `return` the list to the `main()` loop.  However, when we `print()` the list within the main function after running `function1`, it appears to have been modified.  Then, after running `function2`, the list does not appear to be modified further.  Why do you see these different behaviors between `function1` and `function2`?  Answer the question for each function by copying the code below to `task5.py` within your github username directory and adding your explanation to each function as a **function description**.

```
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
(c) 2016 Brant Faircloth || http://faircloth-lab.org/
All rights reserved.

This code is distributed under a 3-clause BSD license. Please see
LICENSE.txt for more information.

Created on 15 February 2016 16:59 CST (-0600)
"""


def function1(l):
    del l[3:5]


def function2(l):
    l = l[1:]


def main():
    my_list = ['a', 'b', 'c', 'd', 'e', 'f']
    function1(my_list)
    print("Here is output from function 1:")
    print(my_list)
    function2(my_list)
    print("Here is output from function 2:")
    print(my_list)


if __name__ == '__main__':
    main()
```
