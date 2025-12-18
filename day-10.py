#Tuples --Ordered & Immutable (cannot change)
colors = ("red", "green", "blue")
colors[0]

#Sets --Unordered & No duplicate values
numbers = {1, 2, 3, 3, 4}
print(numbers)  # duplicates removed

#--Add/Remove
numbers.add(5)
numbers.remove(2)

#Examples
coords = (10, 20)
print(coords[0])

unique_nums = {1, 2, 2, 3}
print(unique_nums)

#Exercise -- Day 10

#A.Tuple
days = ("Mon", "Tue", "Wed", "Thu", "Fri")
print(days[0])
print(days[-1])

#B.Set
nums = {1, 2, 3, 3, 4, 5}
print(nums)
nums.add(6)
nums.remove(2)
print(nums)

#Mini Project -- Unique Name Collector
names = set()

for i in range(5):
    name = input(f"Enter name {i + 1}: ")
    names.add(name)

print("\nUnique Names:")
print(names)
