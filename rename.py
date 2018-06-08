#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, sys
 
print "###########start#####################"

curpath = raw_input("Please intput dir:")
if curpath == "":
	curpath = os.getcwd()
print curpath

name1 = raw_input("Please intput your before key:")
name2 = raw_input("Please intput your after key:")


dirs = os.listdir( curpath )

it = iter(dirs)
while True:
    try:
        x = next(it)

        if x.find(name1) != -1:
        	x2 = x.replace(name1, name2)
        	os.rename(os.path.join(curpath,x), os.path.join(curpath,x2))
        	print("rename:" + x + " to " + x2)
    except StopIteration:
        break

print "###########end#####################"
