#Defining a function
def greet():
    print("Hello!")

#Function with parameter
def greet(name):
    print("Hello", name)

#Function with return
def add(a, b):
    return a + b


#Examples
def square(num):
    return num * num

result = square(10)
print(result)


#Exercise -- Day 8
def greet(name):
    print("Hello", name)

def square(num):
    return num * num

result = square(7)
print(result)


#Mini Project -- Simple Calculator (Using Functions)

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

a = float(input("Enter a number 1:"))
b = float(input("Enter a number 2:"))
print("Addition:", add(a, b))
print("Subtraction:", subtract(a, b))
print("Multiplication:", multiply(a, b))
print("Division:", divide(a, b))
