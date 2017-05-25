#!/usr/bin/env python

__author__ = "Andrea Fioraldi"
__copyright__ = "Copyright 2017, Andrea Fioraldi"
__license__ = "MIT"
__email__ = "andreafioraldi@gmail.com"

import csv
import sys
import random

if len(sys.argv) < 2:
    print "Usage: python split_files_csv.py <number of splitted lists>"

num = int(sys.argv[1])

files = open("files.csv")

arr = []

reader = csv.reader(files)
reader.next() #skip header

for row in reader:
    edb = tuple(row)[0]
    arr.append(edb)

random.shuffle(arr)

avg = len(arr) / float(num)
out = []
last = 0.0

while last < len(arr):
    out.append(arr[int(last):int(last + avg)])
    last += avg

for i in xrange(len(out)):
    f = open("files_" + str(i) + ".list", "w")
    for id in out[i]:
        f.write(id + "\n")
    f.close()

files.close()
