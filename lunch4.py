#!/usr/local/bin/python
import random
import sys
for x in range(int(sys.argv[1])):
	random.seed()
	llist = open("./list","r")
	lunchlist = llist.readlines()
	x = random.randrange(1,len(lunchlist))
	print(lunchlist[x])
