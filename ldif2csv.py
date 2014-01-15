
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

# CSV Header
header = [ "First Name", "Last Name", "Login ID", "Mobile No.",
            "Email ID", "Profile", "Password Policy (y/n)" ]

def write_file():
        with open('ldif.csv','wb') as output_file:
                with open(inputfile) as input_file:
                        writer = csv.writer(output_file, quoting=csv.QUOTE_MINIMAL)
                        writer.writerow(header)
                        myrow = []
                        for line in input_file:
                                if not line.strip():
                                        writer.writerow(myrow)
                                        myrow = []
                                        continue
                                atribute, value = line.split(":")
                                v = map_fileds.get(atribute,"None")
                                if 'pwdPolicySubentry' == atribute:
                                        value = "Yes"
                                else:
                                        pass #myrow.append(value.strip())
                                if v != "None":
                                        myrow.append(value.strip())
                writer.writerow(myrow)

        print myrow
        print header


if __name__ == '__main__':
        inputfile = sys.argv[1]
        write_file()
