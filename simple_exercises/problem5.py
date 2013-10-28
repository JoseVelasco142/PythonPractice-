#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Write a Function translate() that will translate a text into "rövarspråket" (Swedish for "robber's language"). that is doulbe every consonant and place an occurrence of "o" in between. 

For Example : translate("this is fun") should be return string :
tothohisos isos fofunon
"""


def translate(str):
    new_str = []
    for c in str:
        if c not in "aeiou" and not c.isspace():
            s = c + "o" + c
            new_str.append(s)
        else: 
            new_str.append(c)
    return ''.join(new_str)

print "Please Enter text to translate to robber language"
input_char = raw_input("> ")

if input_char:
    print translate(input_char)
