#2. The Greatest Showdown

#Objective:
#Harness the power of conditional statements to compare and determine values.

#Task 1: Identify the Greatest
#Write a Python program that prompts the user to enter three numbers. 
#The program should then identify and print out the largest number 
#among the three.

# Number and input prompts
print("Enter the first number")
a = input()
print("Enter the second number")
b = input()
print("Enter the third number")
c = input()
# setting varables to float
a = float(a)
b = float(b)
c = float(c)

if (a > b) and (a > c):
    print(a , "is the largest number")
elif (b > a) and (b > c):
    print(b , "is the largest number")
else:
    print(c , "is the largest number")

# Task 2: Identify the Smallest
# Extend your program from Task 1 to 
# also determine the smallest number among 
# the three and print it out.

if (a < b) and (a < c):
    print(a , "is the smallest number")
elif (b < a) and (b < c):
    print(b , "is the smallest number")
else:
    print(c , "is the smallest number")

#Task 3: Equality Check
#Enhance your program to handle cases where two or all of 
#the numbers are equal. The program should display appropriate 
#messages like "Two numbers are equal and the largest" or 
#"All numbers are equal".

if (a == b):
    print(a ,"and", b , " are equal")
elif (a == c):
    print(a ,"and", c , "are equal")
elif (b == c):
    print(b ,"and", c , "are equal")
else:
    print("nothing is equal!")