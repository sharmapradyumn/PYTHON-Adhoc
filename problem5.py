#!/usr/bin/python3

import datetime
username=input("enter your name for greeting")
datetime=datetime.datetime.now()
hr=datetime.hour

if hr>=5 and hr<=12:
    print("Goooood morninnnnng "+str(username))

elif hr>=12 and hr<=17:
    print("Gooooood Afternoon "+str(username))
 
elif hr>=17 and hr<=20:

    print("Goooodddd Evening "+str(username))

elif hr>=20 and hr<=5:
    print("Goooodd Night "+str(username))

