#!/usr/bin/env python

# This Script is Advance version of privious script
# Advance means here I will reduce code and make it
# More faster and cleaner 

from __future__ import print_function
import sys

def GetNormalUsers(file):
    """ This Function will return list of normal users
    by reading input passwd file, Basically Normal user UID
    is above 500 """
    with open(file,'r') as f:
        Users = [ l for l in f if int(l.split(':')[2]) >= 500 ]
        print(''.join(Users))

# OLD Version without Listcomprehence
#    with open(file,'r') as f:
#           for line in f:
#               l = line.split(':')
#               if int(l[2]) >= 500:
#                      print(line,end='')
#


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("\nUsage:-\t {0} <PassWdFile>\n".format(sys.argv[0]))
    else:
        try:
            PassWdFile = sys.argv[1]
            GetNormalUsers(PassWdFile)
        except:
            print("Error: Unable to OpenFile {0}".format(sys.argv[1]),file=sys.stderr)
