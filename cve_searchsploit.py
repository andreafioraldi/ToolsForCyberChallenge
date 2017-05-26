#!/usr/bin/env python

__author__ = "Andrea Fioraldi"
__copyright__ = "Copyright 2017, Andrea Fioraldi"
__license__ = "MIT"
__email__ = "andreafioraldi@gmail.com"

import cve_exploitdb_dict
import csv
import sys

if len(sys.argv) < 2:
    print "Usage: python cve_searchsploit.py <cve>"
    print
    sys.exit(1)

cve_map = cve_exploitdb_dict.get_cve_map()

cve = sys.argv[1].upper()

if not cve in cve_map:
    print "ERROR - CVE not found."
    print
    sys.exit(1)

files = open("/usr/share/exploitdb/files.csv")
reader = csv.reader(files)
reader.next() #skip header

for row in reader:
    edb, file, description, date, author, platform, type, port = tuple(row)
    if int(edb) == cve_map[cve]:
        print "Exploit DB Id: " + edb
        print "File: /usr/share/exploitdb/platforms/" + file
        print "Date: " + date
        print "Author: " + author
        print "Platform: " + platform
        print "Type: " + type
        if port != "0":
            print "Port: " + port
        print
        sys.exit(0)
print "ERROR - EDB id not found."
print
sys.exit(1)

