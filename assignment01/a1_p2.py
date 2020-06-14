#Name: Omar Khan
#Student ID: 101168124
dis = int(input("Enter a distance in cm: "))
feet = int(dis//30.48)
inches = int(round((dis%30.48)/2.54))
print(str(dis) + "cm is approximately " + str(feet) + "\'" + str(inches) + "\"")