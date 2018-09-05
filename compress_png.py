#!/usr/bin/python
# -*- coding: UTF-8 -*-

# os.chdir(）

import os
import platform

sysstr = platform.system()
if sysstr == "Darwin":
	cmd_path = os.path.join(os.getcwd(), "pngquant/pngquant")
elif sysstr == "Windows":
	cmd_path = os.path.join(os.getcwd(), "pngquant/pngquant")


print "###########start#####################"
print cmd_path

# cmd_path = os.path.join(os.getcwd(), "pngquant/.//pngquant")
curpath = raw_input("Please intput dir:")
if curpath == "":
	curpath = os.getcwd()
print curpath


def compresspng(cdir):
	print("compress beg:" + cdir)
	os.chdir(cdir)
	cmd = "{cmd_path} --skip-if-larger --verbose --force --ext .png  256 *.png"
	cmd = cmd.format(cmd_path = cmd_path)
	print(cmd)
	os.system(cmd)

compresspng(curpath)
for root, dirs, files in os.walk(curpath, topdown=True):
	index = 0
	while index < len(dirs):
		name = dirs[index]
		if name[0] == '.':
			del dirs[index]
			continue
		print(name)
		proc_path = os.path.join(root, name)
		compresspng(proc_path)
		index += 1


