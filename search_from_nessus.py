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

def do_stuff(file):
	reader = csv.reader(file)
	reader.next() #skip header
	for row in reader:
		cve = tuple(row)[1]
		proto = tuple(row)[5]
		port = tuple(row)[6]
		name = tuple(row)[7]
		print "*"*100
		print "[[" + name + "]]"
		print
		print "CVE: " + cve
		print "Protocol: " + proto
		print "Port: " + port
		print 
		if not cve in get_cve_map:
			continue
		cmd = "searchsploit '/" + get_cve_map[cve.upper()] + ".'"
		out = commands.getstatusoutput(cmd)[1].splitlines(True)
		out = out[4:-2]
		print "\n".join(out)
		print "*"*100
		print

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
