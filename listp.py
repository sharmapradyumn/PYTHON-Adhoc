#!usr/bin/python3

# create a list
adhoc = [1,2,3,22,1,66,44,0,2,6,9]
greater = []
lesser= []
for i in adhoc:
    if i>5:
          greater.append(i)
    elif i<=2:
           lesser.append(i)
 
print("number greater than 5"+str(greater))
print("number greater than 2 and equal"+str(lesser))

