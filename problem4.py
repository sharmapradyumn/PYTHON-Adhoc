#!/usr/bin/python3
import os
p = input("enter your username")
for i in p:
    if i.isalpha()==True:
        os.system('sudo useradd '+str(p))
        os.system('sudo passwd '+str(p))
    elif i.isdigit()==True:
        print("only string character is allowed")
        exit()

