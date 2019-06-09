#!/usr/bin/python3

from googlesearch import search
import time
raw_data=open('search.txt','w')
data=input("Enter something you want to search:-")
for i in search(data,tld="co.in",stop=10):
	print(i)
	raw_data.write(i+" \n")
	time.sleep(1)
raw_data.close()