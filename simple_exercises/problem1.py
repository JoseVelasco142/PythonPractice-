#!/usr/bin/env python

"""
Define a function max() that takes two number as arguments and return the largest of them.
use if-else construct available in python. (it is true that python has max function buit in, but writing it yourself is nevertheless good exercise )
"""
import sys

def max(a,b):
    if a > b:
        return a
    else: return b


if __name__ == '__main__':
    numbers = raw_input("Enter any two Numbers to check max value:- ")
    if len(numbers.split()) == 2:
        a,b = [ int(n) for n in numbers.split() ]
        max_num = max(a,b)
        print "Max Number is :- ", max_num
    else:
        print "Only two numbers are allowed."
        raise SystemExit(1)
    
