#!/usr/bin/env python

# tested with pysmb==1.1.8 & Python 2.4.3

from smb.SMBConnection import SMBConnection
import os
import time
import tarfile
import subprocess

username = 'champu'
password = 'password'
netbios_name = 'desktop' # netbios name of remote server
sharename = 'backup' # share name of remote server
server_ip = '172.16.3.245'
client = subprocess.Popen(['hostname'],stdout=subprocess.PIPE).communicate()[0].strip()

class SmbClient(object):
        def __init__(self,ip,username,password,sharename):
                self.ip = ip
                self.username = username
                self.password = password
                self.sharename = sharename
        def connect(self):
                self.server = SMBConnection(self.username,
                                self.password,client,netbios_name,use_ntlm_v2=True)
                self.server.connect(self.ip,139)
        def upload(self,file):
                data = open(file,'rb')
                file = '/' + file
                self.server.storeFile(self.sharename,file,data)
                print "file has been uploaded"
        def download(self,file):
                fileobj = open(file,'wb')
                self.server.retrieveFile(self.sharename,fileobj)
                print "file has been downloaded in current dir"

        def delete(self,file):
                'remove file from remote share'
                file = '/' + file
                self.server.deleteFiles(self.sharename,file)

        def list(self):
                ' list files of remote share '
                filelist = self.server.listPath(self.sharename,'/')
                for f in filelist:
                        print f.filename

def maketargz(*items):
        date = time.strftime('%d.%m.%Y')
        file = 'indiainfoline_LDAP_' + date + '.tar.gz'
        tar = tarfile.open(file,'w:gz')
        def tardir(dir):
                for root,dirs,files in os.walk(dir):
                        for f in files:
                                try:
                                        tar.add(os.path.join(root,f))
                                except IOError:
                                        pass
                        for d in dirs:
                                try:
                                        tar.add(os.path.join(root,d),recursive=False)
                                except IOError:
                                        pass

        for f in items:
                try:
                        tar.add(f)
                except  IOError:
                        pass
                else:
                        if os.path.isdir(f):
                                tardir(f)
        tar.close()
        return file

def main():
        smb = SmbClient(server_ip,username,password,sharename)
        os.system("ldapsearch -xb 'dc=example,dc=com' > /opt/ldap-srv.ldif")
        bkpfile = maketargz('/opt/ldap-srv.ldif','/etc/openldap/')
        smb.connect()
        smb.upload(bkpfile)
        smb.list()

if __name__ == '__main__':
