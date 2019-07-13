#!/usr/bin/python3

import datetime
user_name=input("Enter your suraj name:-")
user_age=int(input("Enter your age:-"))

# storing value of current date w.r.t year,month and day
current_datetime=datetime.datetime.now()
current_year=current_datetime.year
new_year=current_year-user_age+95
print("Hey "+str(user_name)+" you will turn 95 years old in "+str(new_year))
