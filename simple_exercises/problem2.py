#!/usr/bin/evn python

"""
Define a function max_of_three() that takes three numbers as arguments and return the largest of them.
"""

def max_of_three(a,b,c):
    if a > b:
        if a > c:
            return a
        elif c > a:
            return c
        else: pass
    elif b > a:
        if b > c:
            return b
        else: return c
    else: pass

if __name__ == '__main__':
    numbers = raw_input("Enter any three number to get max number:- ")
    l = numbers.split()
    if len(l) == 3:
        a,b,c = [ int(n) for n in l ]
        print max_of_three(a,b,c)
    else:
        print "Only three number are allowed"
        raise SystemExit(1)

        
