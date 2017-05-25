#!/usr/bin/env python

__author__ = "Andrea Fioraldi"
__copyright__ = "Copyright 2017, Andrea Fioraldi"
__license__ = "MIT"
__email__ = "andreafioraldi@gmail.com"

import sys
import commands

scans = ["", "-sS", "-sT", "-sA", "-sW", "-sM", "-sN", "-sF", "-sX", "-sY", "-sZ"]
policies = ["", "-f", "--data-length 32"]
discovery = ["", "-Pn", "-PS", "-PA", "-PU", "-PY", "-PE", "-PP", "-PN"]

def nmap_probe(host, port):
    i = 0
    for s in scans:
        for p in policies:
			for d in discovery:
				cmd = 'nmap ' + host + ' -p ' + port + ' --version-all ' + s + " " + p + " " + d
				print "Probe " + str(i) + ": " + cmd
				cmd = cmd + ' | grep ' + port + '/tcp | cut -d " " -f 2'
				ret = commands.getstatusoutput(cmd)
				if ret[1] == "closed" or ret[1] == "open":
					print 
					print "Found " + ret[1] + " with: " + s + " " + p
					return
				i += 1
    print
    print "No valid configuration found."

if __name__ == '__main__':
    if len(sys.argv) < 3:
	print "[nmap_conf_prober]"
	print "Copyright 2017, Andrea Fioraldi"
	print
        print "Usage: python nmap_conf_prober.py <host> <port>"
        print
        sys.exit(1)
    h = sys.argv[1]
    p = sys.argv[2]
    nmap_probe(h, p)
    
