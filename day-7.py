#notes

#A. For loop -- Print numbers 1 to 10 using a for loop
#B. While loop -- Print numbers 1 to 5 using a while loop

#For loop (looping through items)
fruits = ["apple", "banana", "mango"]

for f in fruits:
    print(f)

#For loop with range()
for i in range(5):  # 0 to 4
    print(i)

#While loop
count = 1

while count <= 5:
    print(count)
    count += 1

#Break & Continue
for i in range(10):
    if i == 5:
        break  # stop loop completely


#Examples
for i in range(1, 6):
    print("Number:", i)

#Exercise -- Day 7

#a. For loop
for i in range(1,11):
    print("Number:",i)
#b. While loop
count = 1
while count <= 5:
    print (count)
    count += 1

#Mini Project -- Number Analyzer
numbers = []

# Ask user for 5 numbers
for i in range(5):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

print("Numbers:",numbers)
print("Largest:",max(numbers))
print("Smallest:",min(numbers))
print("Sum:",sum(numbers))