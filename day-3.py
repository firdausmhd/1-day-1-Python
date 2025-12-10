#string sequences
name = "Python"     # index:    012345

#indexing
name[0]  # P
name[3]  # h

#negative indexing
name[-1]  # n
name[-2]  # o

#slicing
name[0:3]   # Pyt
name[2:]    # thon
name[:4]    # Pyth

#string methods [upper(), lower(), title(), strip(), replace(), find()]

#string formatting
f"Hello {name}"


#examples
text = "Hello World"

print(text.upper())
print(text[0])
print(text[-1])
print(text[0:5])
print(text.replace("World", "Python"))


#Exercise - Day 3
text = "I am learning Python every day"
print(text[0:5])
print(text[-4:])
print(text.upper())
print(text.replace("Python","Programming"))
print(text.count("a"))

#Mini Project - Name Formatter
first_name = "firdaus"
last_name = "bin ali"
full_name = first_name + " " + last_name
initials = first_name[0] + last_name[0]

print(f"===============================")
print(f"        NAME FORMATTER         ")
print(f"===============================")
print(f"Original : ",full_name)
print(f"Title    : ",full_name.title())
print(f"Upper    : ",full_name.upper())
print(f"Lower    : ",full_name.lower())
print(f"Initials : ",initials.upper())
print(f"===============================")