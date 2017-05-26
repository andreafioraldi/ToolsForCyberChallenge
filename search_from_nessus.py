#!/usr/bin/env python

__author__ = "Andrea Fioraldi"
__copyright__ = "Copyright 2017, Andrea Fioraldi"
__license__ = "MIT"
__email__ = "andreafioraldi@gmail.com"

import sys
import csv
import commands
import cve_exploitdb_dict

cve_map = cve_exploitdb_dict.get_cve_map()

files = open("/usr/share/exploitdb/files.csv")
reader = csv.reader(files)
reader.next() #skip header

def do_stuff(file):
	reader = csv.reader(file)
	reader.next() #skip header
	for row in reader:
		cve = tuple(row)[1]
		proto = tuple(row)[5]
		port = tuple(row)[6]
		name = tuple(row)[7]
		
		if not cve in cve_map:
			continue

		sname = "* " + name + " *"
		print "*"*len(sname)
		print sname
		print "*"*len(sname)
		print
		print "CVE: " + cve
		print "Protocol: " + proto
		print "Port: " + port
		print
		print " +++ Exploit DB matching +++ "
		print
		
		files = open("/usr/share/exploitdb/files.csv")
		reader = csv.reader(files)
		reader.next() #skip header
		
		found = False
		for row in reader:
			edb, file, description, date, author, platform, type, port = tuple(row)
			if int(edb) == cve_map[cve]:
				found = True
				print "Exploit DB Id: " + edb
				print "File: /usr/share/exploitdb/platforms/" + file
				print "Date: " + date
				print "Author: " + author
				print "Platform: " + platform
				print "Type: " + type
				if port != "0":
					print "Port: " + port
				print
		if not found:
			print "ERROR - No EDB Id found"
			print
		print
		files.close()

if __name__ == "__main__":
	if len(sys.argv) < 2:
	    print "Usage: search_from_nessus.py <csv scan file name>"
            print
            sys.exit(1)
	try:
		file = open(sys.argv[1], "r")
	except:
		print "Error: invalid input file"
		print
		sys.exit(1)
	do_stuff(file)
