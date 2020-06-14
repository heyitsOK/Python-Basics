#Name: Omar Khan
#Student ID: 101168124
num1 = int(input("1. Enter a number: "))
num2 = int(input("2. Enter a number: "))
num3 = int(input("3. Enter a number: "))
num4 = int(input("4. Enter a number: "))
big = num1
big = (big > num2)*big + (num2 > big)*num2
big = (big > num3)*big + (num3 > big)*num3
big = (big > num4)*big + (num4 > big)*num4

small = num1
small = (small < num2)*small + (num2 < small)*num2
small = (small < num3)*small + (num3 < small)*num3
small = (small < num4)*small + (num4 < small)*num4
dif = big - small
print("The largest difference is " + str(dif))