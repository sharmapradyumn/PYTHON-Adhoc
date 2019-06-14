#!/usr/bin/python3
from googlesearch import search
import pyqrcode
url=input("search somthing")
lurl=[]
for i in search(url,stop==3):
    lurl.append(i)
    print(i)
    nurl=pyqrcode.create(i)
    for j in rang(3):
        nurl.svg(str(j)+".svg",scale==8)

