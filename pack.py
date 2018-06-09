#!/usr/bin/python
# -*- coding: UTF-8 -*-
#author: dkcao by 2018-06-08

import os, sys
from PyTexturePacker import Packer #pip install PyTexturePacker
 
print "###########start#####################"


curpath = raw_input("Please intput dir:")
if curpath == "":
	curpath = os.getcwd()
print curpath


name1 = raw_input("Please intput name:")
output = os.path.join(curpath,"tmp/")
outfile = os.path.join(output,name1 + "%d")

if not os.path.exists(output):
 os.mkdir(output)

# create a MaxRectsBinPacker
packer = Packer.create(max_width=2048, max_height=2048, bg_color=0xffff00ff)
# pack texture images under directory "test_case/" and name the output images as "test_case".
# "%d" in output file name "test_case%d" is a placeholder, which is a multipack index, starting with 0.
packer.pack(curpath, outfile)

print outfile
print "###########end#####################"

