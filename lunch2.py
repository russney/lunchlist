#!/usr/local/bin/python
import random
random.seed()
x = random.randrange(1,92)
llist = open("./list","r")
print(llist.readlines()[x])
