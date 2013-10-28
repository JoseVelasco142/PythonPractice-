#!/usr/bin/env python


"""
Define a function reverse() that computes the reversal of a string.
For Example: 
reverse("I am testing") should return the string "gnitset ma I"
"""


def reverse(str):
    l = []
    s = len(str)
    for i in range(s,0,-1):
        i -= 1
        l.append(str[i])
    return ''.join(l)


print reverse("I am testing")
print reverse("Rahul Linux")
