import datetime
from math import pi

now = datetime.datetime.now()
print("Current data time:")
print(now.strftime("%Y-%m-%d %H:%M:%S"))

r = float(input("Input the radius of the circle : "))
print("The area of the circle with radius " + str(r) + " is: " + str(pi * r ** 2))
