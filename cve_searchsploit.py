#!/usr/bin/env python

__author__ = "Andrea Fioraldi"
__copyright__ = "Copyright 2017, Andrea Fioraldi"
__license__ = "MIT"
__email__ = "andreafioraldi@gmail.com"

import cve_exploitdb_dict
import csv
import sys

cve_map = cve_exploitdb_dict.get_cve_map()

def _search_cve_aux(cve):
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

    files.close()
    return found

def search_from_file(file):
    for line in file:
        line = line.strip()
        if len(line) == 0:
            continue
        
        print " ++++ " + line + " ++++ "
        cve = line.upper()

        if not cve in cve_map:
            print "ERROR - CVE not found."
            print
            continue

        _search_cve_aux(line)
        print

def search_from_nessus(file):
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
        print " ++++ Exploit DB matching ++++ "
        print
        
        _search_cve_aux(cve)
        print

def search_cve(cve):
    cve = cve.upper()

    if not cve in cve_map:
        print "ERROR - CVE not found."
        print
        sys.exit(1)
    
    found = _search_cve_aux(cve)
    if not found:
        sys.exit(1)
    
    print

def usage():
    print "[cve_searchsploit]"
    print "Copyright 2017, Andrea Fioraldi"
    print
    print "Usage: python cve_searchsploit.py <cve>"
    print "       python cve_searchsploit.py -f <file with cve list>"
    print "       python cve_searchsploit.py -n <nessus csv scan file>"
    print
    sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
    if sys.argv[1] == "-f":
        if len(sys.argv) < 3:
            usage()
        try:
            file = open(sys.argv[2], "r")
            search_from_file(file)
        except Exception as exc:
            print "ERROR - " + str(exc)
            print
            sys.exit(1)
    elif sys.argv[1] == "-n":
        if len(sys.argv) < 3:
            usage()
        try:
            file = open(sys.argv[2], "r")
            search_from_nessus(file)
        except Exception as exc:
            print "ERROR - " + str(exc)
            print
            sys.exit(1)
    else:
        search_cve(sys.argv[1])
