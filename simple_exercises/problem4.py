#!/usr/bin/env python

"""
Write a function that takes a character ( a string 1 length ) and return True if it is vowel, 
False otherwise.
"""

def check_vowel(a):
    vowel = "aeiou"
    if a in vowel:
        return True
    else:
        return False


if __name__ == '__main__':
    char = raw_input("Enter a Single Character to Check Vowel : - ")
    if len(char) == 1:
        print check_vowel(char)
    else:
        print "Only 1 character is allowed"
        raise SystemExit(1)
