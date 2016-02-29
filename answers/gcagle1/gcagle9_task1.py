#! /usr/bin/env python
# encoding: utf-8

'''
Program demonstrating 5 different string methods.
Grace Cagle
22 Feb 2016
Assignment 9 Task 1
'''

thing = """The most beautiful thing we can experience is the mysterious.
\t\t\t\t\t\tIt is the source of all true art and science."""


def find_length(a):
    return(len(a))


def make_title(a):
    return(thing.title())


def make_uppercase(a):
    return(thing.upper())


def count_letter(a):
    return(thing.count("a"))


def find_word(a):
    return(thing.find("thing"))


def main():
    print("This is our string: " + thing)
    print("The length method: \nThe length of our string is: ",
        find_length(thing))
    print("The title method: \nOur string as a title looks like this:",
        make_title(thing))
    print("The uppercase method: \nOur string in uppercase look like this: ",
        make_uppercase(thing))
    print("The count method: \nThe number of a's in our string is: ",
        count_letter(thing))
    print("""The find method: \nFinds the position of a given word \"thing\"
    in our string: """, find_word(thing))

if __name__ == '__main__':
    main()
