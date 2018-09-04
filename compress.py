#!/usr/bin/python
# -*- coding: UTF-8 -*-
#author: dkcao by 2018-06-08

import os, sys

def jwkj_get_filePath_fileName_fileExt(filename):
    (filepath,tempfilename) = os.path.split(filename);
    (shotname,extension) = os.path.splitext(tempfilename);
    return filepath,shotname,extension

def astrcmp(str1,str2):
    return str1.lower()==str2.lower()

print "###########start#####################"

curpath = raw_input("Please intput dir:")
if curpath == "":
	curpath = os.getcwd()
print curpath

def compress(cdir):
	print("compress beg")

	dirs = os.listdir( cdir )

	it = iter(dirs)
	while True:
	    try:
	        x = next(it)
	        if x[0] != '.':
		        fullpath = os.path.join(cdir,x)

		        if os.path.isdir(fullpath):
		        	compress(fullpath)
		        	continue

	        	(filepath,shotname,extension) = jwkj_get_filePath_fileName_fileExt(fullpath)
	        	   	

	        	if astrcmp(extension , '.png' ) or astrcmp(extension , '.jpg') or astrcmp(extension , '.jpeg' ) :
	        		print(filepath,shotname,extension)

	        		# 7z a -tgzip poker_hall_hall_bg.gz poker_hall_hall_bg.png
	        		zipfile = os.path.join(cdir,shotname + ".gz")
	        		cmd = "7z a -tgzip {zipfile} {picfile}"
	        		cmd = cmd.format(zipfile = zipfile, picfile = fullpath)
	        		print(cmd)
	        		os.system(cmd)
	        		cmd_move = "move {src} {dest}"
	        		cmd_move = cmd_move.format(src = zipfile, dest = fullpath)
	        		print(cmd_move)
	        		os.system(cmd_move)

	    except StopIteration:
	        break

compress(curpath)


# if __name__ == '__main__':  
# 	compress()

# 	print "###########end#####################"

