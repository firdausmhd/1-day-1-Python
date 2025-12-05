#example_1
x = 10
y = "20"

print(type(x))       # int
print(type(y))       # str

z = int(y)
print(z + x)         # 30
---------------------------------
x = 10.1
y = "24"
print(type(x))
print(type(y))
z = int(y)
print(z+x)


#Exercise-day-2
s = 23
t = 170.1
u = "Firdaus"
v = True

print("Value:",s,", Type:",type(s))
print("Value:",t,", Type:",type(t))
print("Value:",u,", Type:",type(u))
print("Value:",v,", Type:",type(v))


#mini-project-2
print("===========================")
print("   VARIABLE INFO TABLE     ")
print("===========================")
print("Name      :",u)
print("Age       :",s)
print("Is Adult  :",v)
print("Height    :",t)
print("===========================")


---auto_alignment
print(f"Name      : {u}")
print(f"Age       : {s}")
print(f"Is Adult  : {v}")
