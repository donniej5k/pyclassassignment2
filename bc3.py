#3. Leap Year Explorer
#Task 1: Leap Year Checker

print("Please input a year to see if it is a Leap Year")
y = input()
y = int(y)

if (y%4 == 0 and y%100 != 0) or (y%400 == 0):
    print("The year",y,"is a Leap Year!!")
else:
    print("The year",y,"is not a Leap Year")

