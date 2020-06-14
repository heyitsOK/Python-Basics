#Name: Omar Khan
#Student ID: 101168124
import math

print("Enter the three side lengths of a triangle: ")
a = int(input("Side 1: "))
b = int(input("Side 2: "))
c = int(input("Side 3: "))

s = (a+b+c)/2

area = math.sqrt((s)*(s - a)*(s - b)*(s - c))

print("A triangle with side lengths " + str(a) + ", " + str(b) + ", and " + str(c) + " has an area of " + str(round(area,4)))