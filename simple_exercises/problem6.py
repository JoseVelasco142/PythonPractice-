#!/usr/bin/env python

"""
Define a function sum() and a function multiply() that sums and multiplies (respectively) 
all the numbers in a list of numbers. 
For Example : 
sum([1,2,3,4]) should return 10
multiply([1,2,3,4]) should return 24
"""


def sum(l):
    b = 0
    for n in l:
        n = n + b 
        b = n
    return n

print sum([1,2,3,4])

def multiply(v):
    b = 1
    for n in v:
        n = n * b
        b = n
    return n


print multiply([1,2,3,4])
