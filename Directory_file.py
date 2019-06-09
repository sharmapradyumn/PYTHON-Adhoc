#!/usr/bin/python3

import os
dirname=input("Enter full path where you want to make files and directory:-")
if not  os.path.exists(dirname):
	os.mkdir(dirname)
# creating 200 directories
	for i in range(1,201):
		os.system("mkdir "+dirname+"/Dir"+str(i))
#creating 100 text files
	for i in range(1,101):
		os.system("touch "+dirname+"/file"+str(i)+".txt")
else:
	
	for i in range(1,201):
		os.system("mkdir "+dirname+"/Dir"+str(i))
	for i in range(1,101):
		os.system("touch "+dirname+"/file"+str(i)+".txt")
	