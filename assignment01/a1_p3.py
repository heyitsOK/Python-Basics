#Name: Omar Khan
#Student ID: 101168124
print("Please enter your grade on the following pieces of work: ")
a1 = int(input("Assignment 1 (/18): "))
a2 = int(input("Assignment 2 (/22): "))
a3 = int(input("Assignment 3 (/15): "))
a4 = int(input("Assignment 4 (/30): "))
mid = int(input("Midterm (/35): "))
final = int(input("Final Exam (/50): "))

a1p = a1/18
a2p = a2/22
a3p = a3/15
a4p = a4/30
midp = mid/35
finalp = final/50

a1w = a1p*0.1
a2w = a2p*0.1
a3w = a3p*0.1
a4w = a4p*0.1
midw = midp*0.25
finalw = finalp*0.35

finalg = (a1w+a2w+a3w+a4w+midw+finalw) * 100

print("Your grades:")
print("-=====================-")
print("Assignment 1:\t" + str(round(a1p*100,2)) + "%")
print("Assignment 2:\t" + str(round(a2p*100,2)) + "%")
print("Assignment 3:\t" + str(round(a3p*100,2)) + "%")
print("Assignment 4:\t" + str(round(a4p*100,2)) + "%")
print("Midterm:\t" + str(round(midp*100,2)) + "%")
print("Final Exam:\t" + str(round(finalp*100,2)) + "%")
print("-=====================-")
print("Your final grade is " + str(round(finalg,2)) + "%")