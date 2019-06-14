#!/usr/bin/python3
import time
option = input('''(i) enter 1 for show the content of a single file
         (ii) enter 2 for multiple file data
         (iii)enter 3 for insert the data 
         (iV) enter 4 for show the no. of lines
         ''')
if option== '1' :
    filh=input("enter your file name::-")
    filo=open(filh)
    print(filo.read())
    filo.close()

elif option=='2' :
    filh=input("enter your file names::-").split()
    for i in filh :
       filo=open(i)
       print(filo.read())
       filo.close()

elif option=='3' :
    filh=input("enter file name::-")
    filo=open(filh,'a')
    text=input("enter the data that you want to write")
    filh.write(text)
    filo.close()
elif option=='4' :
     filh=input("enter file name::-")
     filo=open(filh)
     text=filo.readlines()
     for i in range(1,len(text)+1):
              print(i,text[i-1])
else : 
         print("option doesn't exist")


