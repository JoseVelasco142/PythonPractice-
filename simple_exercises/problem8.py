#!/usr/bin/env python


"""
Define a function is_palidrome() that recognizes palidromes ( i.e words that look the same  written
backwards). For example is_palidrome("radar") shold return True
"""

def reverse(str):
    l = []
    s = len(str)
    for i in range(s,0,-1):
        i -= 1
        l.append(str[i])
    return ''.join(l)


def is_palidrome(str):
    if str.lower() == reverse(str.lower()):
        return True
    else:
        return False

print "Word radar is_palidrome", is_palidrome("radar")
print "Word lol is_palidrome", is_palidrome("lol")
print "Word linux is_palidrome", is_palidrome("linux")

words = [ "Dewed", "civic", "peeweep", "madam" , "Notso,Boston"]

for w in words:
    print "Word %s is_palidrome %r" % ( w, is_palidrome(w))


