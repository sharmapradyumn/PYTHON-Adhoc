#!/usr/bin/python3
s = input("enter a string")
i=0
s1=""
for x in s:
    if s.index(x)==i:
        s1+=x
    i+=1
print("removed character string is")
print("\n")
print(s1)