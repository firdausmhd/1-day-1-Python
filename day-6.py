#creating a list
fruits = ["apple", "banana", "orange"]
print(fruits)

#access by index
fruits[0]   # "apple"
fruits[2]   # "orange"

#modify element
fruits[1] = "mango"

#add items
fruits.append("grape")
fruits.insert(1, "kiwi")

#remove items
fruits.remove("apple")   # removes by value
fruits.pop(2)            # removes by index

#examples
numbers = [5, 3, 8, 1]
numbers.append(10)
numbers.sort()
print(numbers)

#Exercise - Day 6
numbers = [10, 20, 30, 40, 50]

print(numbers[0])
print(numbers[4])
numbers[1]=25
numbers.append(60)
numbers.pop(-2)
print(numbers)

#Mini Project- Shopping List Manager
shopping = ["milk", "bread", "rice"]

new_item = input("Enter item to add: ")
shopping.append(new_item)

remove_item = input("Enter item to remove: ")
if remove_item in shopping:
    shopping.remove(remove_item)
else:
    print(remove_item, "is not in the shopping list.")

print("Final shopping list:", shopping)