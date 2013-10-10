#!/usr/bin/env python
'''
This Script Simply Generate Ldap custum attrubute 
it will read object.txt from current path and generate list
in input file each object on each line

WARNING!!!
oid number should be uniq, So you need to make sure
the old which is use in this script should not be already used

Reference Link
http://www.yolinux.com/TUTORIALS/LinuxTutorialLDAP-DefineObjectsAndAttributes.html#OBJECT
'''
import shutil
import time
import subprocess

objectclass_name = 'flexeraAccount'
object_class_description = 'Additional account properties'
superior_objectclass = 'top'
#object_type = 'STRUCTURAL'
object_type = 'AUXILIARY'
oid_num_end = 101

# Save details in following files
file_attributes_schema = objectclass_name + '_attributes.schema'
file_object_schema = objectclass_name + '_object.schema'




attribute_format = """attributetype ( 1.3.6.1.4.1.4203.666.1.%d
        NAME '%s'
        EQUALITY caseIgnoreMatch
        SUBSTR caseIgnoreSubstringsMatch
        SYNTAX 1.3.6.1.4.1.1466.115.121.1.15{1024} )
	"""

new_schema = """
objectClass     ( 1.3.6.1.4.1.4203.666.1.100
    NAME  '%s'
    	DESC  '%s'
    SUP %s                     	
    %s                   	
        MAY  (  
               %s 
		
		) 
        )
"""


objects_file = 'object.txt'
object_list = []

read_object = open(objects_file,'r')
write_attribute_schema = open( file_attributes_schema, 'w' )

for obj in read_object:
	obj = obj.strip()
	if obj.startswith('#'): continue # skipp commented
	
	# Create list for new Object class
	object_list.append(obj)
	object_list.append(' $ ')


	# check object attrubute already define or not if define then skip that 
	p = subprocess.Popen('grep -m1 -R %s /etc/openldap/' % obj ,stdout=subprocess.PIPE,shell=True)
	if p.communicate()[0]: continue

	print >>write_attribute_schema,attribute_format % ( oid_num_end, obj )
	oid_num_end += 1
	

object_list.pop() # remove last $ from list 
write_object_schema = open( file_object_schema, 'w' )

print >>write_object_schema,  new_schema % ( 	objectclass_name, object_class_description, 
						superior_objectclass, object_type, ''.join(object_list) )

print """
Schema File has been created as below
 
%s 
%s

Now you can add in your slapd.conf 

include         /etc/openldap/schema/%s
include         /etc/openldap/schema/%s
""" % ( file_attributes_schema,file_object_schema,file_attributes_schema,file_object_schema )

write_attribute_schema.close()
write_object_schema.close()

shutil.copy2( file_attributes_schema, '/etc/openldap/schema/' + file_attributes_schema )
shutil.copy2( file_object_schema, '/etc/openldap/schema/' + file_object_schema )
