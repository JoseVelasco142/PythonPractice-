#!/usr/bin/env python


# LDIF to CSV Converter 

import csv
import sys

# Skip entries
skip = [ "dn", "loginShell", "uid", "gid", "cn", 
	 "userPassword","uidNumber", "gidNumber",
	 "homeDirectory", "displayName", 
	 "objectClass", "uidNumber"  ]

# CSV Header field
map_fileds = dict(  givenName = "First Name",
                    sn = "Last Name",
                    uid = "Login ID",
                    telephoneNumber = "Mobile No.",
                    mail = "Email ID",
                    Profile = "Profile",
                    pwdPolicySubentry = "Password Policy (y/n)"
		)

def readfile(file):
	ldif_file = open(file,'r')
	try:
		for line in ldif_file:
			atribute, value = line.split(":")
			if atribute not in skip:
				if 'pwdPolicySubentry' == atribute:
					value = "Yes"
					print map_fileds.get(atribute,"None"), value,
				else:
					print map_fileds.get(atribute,"None"), value,
	finally:
		ldif_file.close()


if __name__ == '__main__':
	inputfile = sys.argv[1]
	readfile(inputfile)
