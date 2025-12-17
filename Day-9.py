#Creating a dictionary
person = {
    "name": "Firdaus",
    "age": 33,
    "language": "Python"
}

#Access values
print(person["name"])

#Add/update values
person["age"] = 34
person["country"] = "Malaysia"

#Remove values
del person["age"]

#Loop through dictionary
for key, value in person.items():
    print(key, ":", value)

#Examples
student = {"name": "Ali", "score": 85}

student["score"] = 90

for k, v in student.items():
    print(k, v)


#Exercise -- Day 9
car = {
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2020
}

print(car["model"])
car["year"] = 2023
car["color"] = "white"
for x, y in car.items():
    print(x, y)

#Mini Project -- Student Record System
student = {
    "Name": "Firdaus",
    "Age": 33,
    "Marks": 92
           }

student["Marks"]=98
student["Grade"]="A"

print(f"Student Record")
print(f"--------------")
for x, y in student.items():
    print(x, ":",y)