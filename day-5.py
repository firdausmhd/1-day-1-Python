#theory
==   # equal
!=   # not equal
>    # greater than
<    # less than
>=   # greater or equal
<=   # less or equal

age = 20

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

#Example
num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

#Exercise-day-5
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

#Mini Project - Simple grade System
num = int(input("Enter your marks (0-100): "))

if num >= 90:
    print("Grade A")
elif num >= 80:
    print("Grade B")
elif num >= 70:
    print("Grade C")
elif num >=60:
    print("Grade D")
else:
    print("Fail")