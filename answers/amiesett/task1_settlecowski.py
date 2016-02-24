#!/usr/bin/env python
# encoding: utf-8

"""
BIOL7800 Assignment 9 Task 1

Amie Settlecowski
25 Feb. 2016

This program demonstrates the use of 5 different string methods.
"""


def method1(list_of_str):
    return ''.join(list_of_str)


def method2(quote):
    return quote.isalpha()


def method3(quote, substr):
    return quote.count(substr)


def method4(quote, old_substr, new_substr):
    return quote.replace(old_substr, new_substr)


def method5(quote, substr):
    return quote.find(substr)


def main():
    l = []
    l.append('The most beautiful thing we can experience is the mysterious.')
    l.append(' It is the source of all true art and science.')

    # 1. joins strings from an iterable
    quote = method1(l)
    print("Output of method1: .join() ")
    print(quote, "\n")

    # 2. determines whether all characters of a string are alphabetic
    if method2(quote):
        print("Output of method2: .isalpha() ")
        print("Quote is alphabetic.", "\n")
    else:
        print("Output of method2: .isalpha()")
        print("Quote includes at least 1 non-alphabetic character.", "\n")

    # 3. counts the number of specified substring in specified string
    substr = 'the'
    substr_count = method3(quote, substr)
    print("Output of method3: .count() ")
    print("'", substr, "' occurs in quote ", substr_count, ' times.', "\n")

    # 4. replaces a substring in original string with new substring
    old_substr = "It"
    new_substr = "Mystery"
    edited_quote = method4(quote, old_substr, new_substr)
    print("Output of method4: .replace() ")
    print(edited_quote, "\n")

    # 5. finds the starting index of specified substring
    substr = "is"
    substr_index = method5(quote, substr)
    print("Output of method5: .find() ")
    print("'", substr, "' first occurs at index", substr_index)

if __name__ == '__main__':
    main()
