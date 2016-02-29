#!/usr/bin/env python

"""
Task 1:
Here is a quote from Albert Einstein:

"The most beautiful thing we can experience is the mysterious. It is the source
 of all true art and science." This quote is also a string. Write a program
 that includes 5 different functions each of which demonstrates one of 5
 different string methods. As always, your program should contain a main loop
 and an ifmain statement.

Created by Shraddha Shrestha on February 24, 2016.
Copyright 2016 Shraddha Shrestha. All rights reserved.

 """


def count_quote(x):
    # To count the number of any letter in the following quote.
    quote = "The most beautiful thing we can experience is the mysterious. It\
 is the source of all true art and science."
    count = 1
    for item in quote:
        if item == x:
            count = count + 1
    return count


def quote_upper():
    # To capitalize every letter in the quote.
    quote = "The most beautiful thing we can experience is the mysterious. It\
 is the source of all true art and science."
    capitalized_quote = quote.upper()
    return capitalized_quote


def quote_split():
    # To split the quote in its characters.
    quote = "The most beautiful thing we can experience is the mysterious. It\
 is the source of all true art and science."
    split_quote = quote.split(' ')
    return split_quote


def replace_string():
    # Replaces two words in the quote.
    quote = "The most beautiful thing we can experience is the mysterious. It\
 is the source of all true art and science."
    return quote.replace("true art", "misery").replace("science", "anger")


def length_string():
    # Find the length of quote.
    quote = "The most beautiful thing we can experience is the mysterious. It\
 is the source of all true art and science."
    return len(quote)


def main():
    result = count_quote("t")
    print("\nThe number of t in the quote above is: \n", result)
    quote_uppercase = quote_upper()
    print("\nThe capitalized quote is: \n", quote_uppercase)
    result = quote_split()
    print("\nThe split characters of quote are: \n", result)
    result = replace_string()
    print("\nModified code: \n", result)
    result = length_string()
    print("\nLength of the string (quote): \n", result)


if __name__ == '__main__':
    main()
