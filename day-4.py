#examples

age = input("Enter your age: ")
print(type(age))  # This will be <class 'str'>

age = int(age) # Convert to integer

------------------------
name = input("Enter your name: ")
age = input("Enter your age: ")

age = int(age)

print("Hello", name)
print("Next year you will be", age + 1)

#Exercise - Day 4
name = input("Enter your name: ")
age = input("Enter your age: ")

age = int(age)

print(f"Hello",name)
print(f"You are",age,"years old.")
print(f"Next year you will be", age + 1,"years old.")



#Mini Project - Simple Calculator
first = input("Enter your first number: ")
second = input("Enter your second number: ")

first = int(first)
second = int(second)

print(f"Addition    :",first + second)
print(f"Subtraction :",first - second)
print(f"Multiplication :",first * second)
print(f"Division :",first / second)