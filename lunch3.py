#!/usr/local/bin/python
import random
random.seed()
llist = open("./list","r")
lunchlist = llist.readlines()
x = random.randrange(1,len(lunchlist))
print(lunchlist[x])
