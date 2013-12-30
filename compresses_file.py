#!/usr/bin/env python

# This Script will compress One day old file means yesterday files

from __future__ import print_function
import os
import sys
import time
import glob
import gzip
import cStringIO
from datetime import datetime

nday=1			# set how many days old file
ftype="*.sh"		# set file type which should be compressed
lookinto="/tmp/"	# path of files


class CheckFile(object):
	'Operation on file like get size,file time etc..'
	def __init__(self,fname):
		self.fname = fname
	def size(self):
		'print size in bytes MB'
		size = int(os.path.getsize(self.fname))
		if size < 1023:
			return `size` + ' byte '
		elif size > 1023 and size <= 102400:
			return `(size >> 10)` + ' kB '
		elif size > 102400:
			return `(size >> 20)` + ' MB '
		else:	return size
	def date(self):
		'print file date'
		self.unix_time = os.path.getmtime(self.fname)
		self.file_date = datetime.fromtimestamp(self.unix_time)
		return self.file_date.strftime('%d/%m/%y')
	def days_of_days_old(self):
		'print how much file is old from today'
		self.date()
		days = (datetime.today() - self.file_date).days
		return days 
		
def compresse_file(file):
	gzfile = file + ".gz"
	fgz = cStringIO.StringIO()
	gzip_file = gzip.GzipFile(filename=file,
		mode='wb',fileobj=fgz)
	gzip_file.write(gzfile)
	gzip_file.close()
	gzfile.close()
	#os.unlink(file)
	

if __name__ == '__main__':
	os.chdir(lookinto)
	print('{0:10}{1:10}{2:10}'.format("Size","Date","File Name"))
	for file in glob.glob(ftype):
		f = CheckFile(file)
		if f.days_of_days_old() == nday:
			print('{0:10}{1:10}{2:10}'.format(f.size(),f.date(),f.fname))
			print("Compressing...")
			compresse_file(file)
			print("file status after compressesion")
			f = CheckFile(file + ".gz")
			print('{0:10}{1:10}{2:10}'.format(f.size(),f.date(),f.fname))
