# !/usr/bin/env python
# encoding: utf-8


"""
My Einstein program
Created by Andre Moncrieff on 23 Feb 2016.
Copyright 2016 Andre E. Moncrieff. All rights reserved.
"""

# I left quote on one line so as not to introduce newline character
quote = "The most beautiful thing we can experience is the mysterious. It is the source of all true art and science."


def all_caps(some_string):
    output = some_string.upper()
    return output


def cap_first_letters(some_string):
    output = some_string.title()
    return output


def count_periods(some_string):
    output = some_string.count(".")
    return output


def split_sentences(some_string):
    output = some_string.split(".")
    return output[0:2]


def does_it_end_with_period(some_string):
    output = some_string.endswith(".")
    return output


def main():
    print("\nOriginal quote:\n" + quote)
    all_cap = all_caps(quote)
    print("\nAll caps:\n" + all_cap)
    cap_first_letter = cap_first_letters(quote)
    print("\nFirst letters capitalized:\n" + cap_first_letter)
    count_period = count_periods(quote)
    print("\nNumber of periods:\n" + str(count_period))
    split_sentence = split_sentences(quote)
    print("\nSentences separated:\n" + str(split_sentence))
    does_it_end_with_per = does_it_end_with_period(quote)
    print("\nTrue or False: does quote end with a period?\n" +
          str(does_it_end_with_per))

if __name__ == '__main__':
    main()
