Modes:

"w" → write (overwrite)
"a" → append
"r" → read

#Writing to a file
with open("data.txt", "w") as file:
    file.write("Hello Python")

#Reading from a file
with open("data.txt", "r") as file:
    content = file.read()
    print(content)

#Examples
with open("names.txt", "a") as f:
    f.write("Firdaus\n")

#Exercise -- Day 11
name = input("Enter your name:")
with open("names.txt", "w") as n:
    n.write(name)
with open("names.txt", "r") as n:
    content = n.read()
    print(content)

#Mini Project -- Simple Notes App
notes = input("Enter a note:")
with open("notes.txt", "w") as note:
    note.write(notes)
with open("notes.txt", "r") as note:
    content = note.read()
    print("Saved Notes:")
    print("-", content)
