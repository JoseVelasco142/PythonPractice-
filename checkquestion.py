#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import tarfile
from StringIO import StringIO
 
import  os
import  sys
import  time
import  subprocess


class Main:
        
     def __int__(self):
         pass

     def title(self):
         os.system('clear')
         print "-" * 50
         print "\tLinux Basic Advance Practical Exame"
         print "-" * 50

     def ask(self,question,ans=''):
        tty_width = subprocess.check_output('tput cols',shell=True)
        msgsize = len(question)
        cols = ( (int(tty_width) - msgsize) - 85 )
        while True:
             if ans == '' or ans is None:
                print question, '-' * cols,
                ans = raw_input('> ')
             else: return ans

     def info(self):
         self.title()
         name = self.ask("Enter Name")
         batch_name = self.ask("Enter Batch Name")
         email_id = self.ask("Enter your Email ID")
         t = time.localtime()
         date = time.strftime('%d/%m/%Y',t)
         return { "Name": name, "Batch": batch_name, "Email ID": email_id, "Date": date }



def progress(a,ans=''):
    print a
    print '-' * 70
    for i in range(10):
        sys.stdout.write('\r')
        print "Checking....",	
        sys.stdout.write("%-20s" % ('.'*i,))
        sys.stdout.flush()
        time.sleep(0.25)
    if ans == True: 
        print "Correct" 
    else: print "Wrong"
    print 
    time.sleep(0.5)


def CheckAns():
    """ This Func will Check all question which is define in Doc ID 101
    If ans is correct then it will return True else False """
    marks = {}
    def Pass(value):
        """ Auto increment marks dict """
        n = len(marks)
        n += 1
        marks[n] = value
    print "\n>>>>>>>>>>>> Paper Checking Started <<<<<<<<<<<<<<<<\n"
    time.sleep(0.5)
    #-----------------------------------------------------------------------------
    try:
        # Q1. Create file "/tmp/data1.img" and "/tmp/data2.img" with size 100M. 
        if int(os.path.getsize('/tmp/data1.img') >> 20) == 100 and int(os.path.getsize('/tmp/data2.img') >> 20) == 100:
            Pass(True)
            p=True
    except:
            Pass(False)
            p=False
    finally:
            progress('Q1. Create file "/tmp/data1.img" and "/tmp/data2.img" with size 100M',p)
     #-----------------------------------------------------------------------------
     # Q2. create box_compress.tar.gz in /tmp/, compress data1.imp and data2.imp in it.
    sio = "/tmp/box_compress.tar.gz"
    try:
        tf = tarfile.open(sio)
        Pass(True)
        p=True
    except:
        Pass(False)
        p=False
    finally:
            progress('Q2. create box_compress.tar.gz in /tmp/, compress data1.imp and data2.imp in it.',p)
     #-----------------------------------------------------------------------------
    try:
        # Q3. Create command called /opt/mycmd, it should be print current date 
        fpath = "/opt/mycmd"
        if os.path.isfile(fpath) and os.access(fpath,os.X_OK):
            Pass(True)
            p=True
        else:
            Pass(False)
            p=False
    except:
            Pass(False)
            p=False
    finally:
            progress('# Q3. Create command called /opt/mycmd, it should be print current date',p)
      #-----------------------------------------------------------------------------
    try:
        # Q4. Create Soft/Hard link of mycmd in /bin/ but if you delete any one, it should not be impact on other. 
        spath = "/bin/mycmd"
        if os.path.islink(spath) and os.path.realpath(spath) == fpath:
            Pass(True)
            p=True
        else:
            Pass(False)
            p=False
    except:
            Pass(False)
            p=False
    finally:
            progress('Q4. Create Soft/Hard link of mycmd in /bin/ but if you delete any one, it should not be impact on other',p)
    return marks


student_info = Main()
student_details = student_info.info() 
CheckAns()


#print student_details
#print checkans
