#theory
#example without error handling
num = int(input("Enter a number: "))

#example with error handling
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid number")


#Examples
try:
    x = int(input("Enter number: "))
    print(10 / x)
except ValueError:
    print("Please enter a number")
except ZeroDivisionError:
    print("Cannot divide by zero")

#Exercise -- Day 12
try:
    x = int(input("Enter number:"))
    print(x)
except ValueError:
    print("Invalid input")

#Mini Project -- Safe Calculator
try:
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    result = float(num1 / num2)
    print("Result:", result)
except ValueError:
    print("Please enter a number")
except ZeroDivisionError:
    print("Cannot divide by zero")
