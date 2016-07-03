#!/usr/bin/env python

"""
A palindrome is a word, phrase, number or other sequence of units that has the property of reading the same in either direction
"""

### Pythonic way using data structure 
#def is_palindrom(data):
#    return str(data)[::-1] == str(data)


### Non pythonic way but using algoritham
def is_palindrom(data):
   data = str(data)
   data_length = len(data)
   i = 0
   while i <= data_length/2:
      if data[i] != data[data_length-1-i]:
         return False
      i += 1
   return True


print is_palindrom(11)
print is_palindrom("rahul")
print is_palindrom("ana")
