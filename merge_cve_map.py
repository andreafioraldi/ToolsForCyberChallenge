#!/usr/bin/env python

__author__ = "Andrea Fioraldi"
__copyright__ = "Copyright 2017, Andrea Fioraldi"
__license__ = "MIT"
__email__ = "andreafioraldi@gmail.com"

out = open("cve_exploitdb_dict.py", "w")

s = "__cve_map = {\n"

i = 0
while True:
    try:
        file = open("files_" + str(i) + ".list.dict")
    except: break
    lines = file.readlines()
    for l in lines:
        s += "\t" + l.strip() + ",\n"
    file.close()
    i += 1

s = s[:-3]
s += "\n}\n\ndef get_cve_map():\n\treturn __cve_map\n"

out.write(s)
out.close()
