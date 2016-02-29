#!/usr/bin/env python
# utf-8

"""
Assignment 8, Task 1
Jon Nations on 14 February 2016

"""

al_string = "The most beautiful thing we can experience is the mysterious. It is the source of all true art and science."


def counting():
    # counts the number of "o's" in the string
    print(al_string.count("o"))


def finder():
    # finds the position of the word "mysterious"
    print(al_string.find("mysterious"))


def splits():
    # splits the two sentences into two strings
    print(al_string.split("."))


def up():
    # makes all lettes uppercase
    print(al_string.upper())


def replacing():
    # replaces "beautiful" with "magnanimous"
    print(al_string.replace("beautiful", "magnanimous"))


def main():
		counting()
		finder()
		splits()
		up()
		replacing()


if __name__ == '__main__':
    main()
