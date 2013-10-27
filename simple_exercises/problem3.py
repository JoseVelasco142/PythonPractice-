#!/usr/bin/env python

"""
Define a function that computes the length of a given list of string 
( it is true that Python has  the len() function built in, but writing,
it yourself nevertheless a good exercise )
"""

def length(str):
    #count = 0
    total = 0
    for c in str:
        total += 1
    return total


print length("Rahul Kisan Patil")
print len("Rahul Kisan Patil")
