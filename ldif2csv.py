#!/usr/bin/env python

# LDIF to CSV Converter
import csv
import sys

# Skip entries
skip = [ "dn", "loginShell","gid", "cn",
         "userPassword","uidNumber", "gidNumber",
         "homeDirectory", "displayName",
         "objectClass", "uidNumber"  ]

# CSV Header
header = [ "First Name", "Last Name", "Login ID", "Mobile No.",
           "Email ID", "Profile", "Password Policy (y/n)" ]

def write_file():
        with open('ldif.csv','wb') as output_file:
                with open(inputfile) as input_file:
                        writer = csv.writer(output_file, 
                quoting=csv.QUOTE_MINIMAL)
                        writer.writerow(header)
                        myrow = []
                        for line in input_file:
                                if not line.strip():
                                        writer.writerow(myrow)
                                        myrow = []
                                        continue
                                atribute, value = line.split(":")
                if atribute in skip: continue
                                if 'pwdPolicySubentry' == atribute:
                                        value = "Yes"
                                else:
                                        pass #myrow.append(value.strip())
                                myrow.append(value.strip())
                writer.writerow(myrow)



if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "\nUsage\n\t{0} <ldif_file>\n".format(sys.argv[0])
        raise SystemExit(1)
    else:
            inputfile = sys.argv[1]
            write_file()
        print "Exported in file : ldif.csv"
