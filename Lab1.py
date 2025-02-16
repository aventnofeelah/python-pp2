import random

print("Hello, world")

if 5 > 2:
    print("Five is greater than two")

x = 5
y = "John"
print(x)
print(y)

x = str(3)
y = int(3)
z = float(3)
print(type(z))
print(type(x))

x, y, z = "Orange", "Banana", "Cherry"
print(x + y + z)

x = y = z = "Orange"
print(x + y + z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = "awesome"
def myFunc():
    x = "fantastic"
    print("Python is " + x)
myFunc()
print("Python is " + x)

x = "awesome"
def myFunc():
    global x
    x = "fantastic"
myFunc()
print("Python is " + x)

x = "Hello World"
print(x)
x = 20
print(x)
x = 20.5
print(x)
x = 1j
print(x)
x = ["apple", "cherry", "banana"]
print(x)
x = ("apple", "banana", "cherry")
print(x)
x = range(0, 6)
print(x)
x = {"name" : "John"}
print(x)
x = {"apple", "banana", "cherry"}
print(x)
x = True
print(x)
x = b"Hello"
print(x)
x = None
print(x)

x = 5 #int
y = 5.1 #float
z = 5j #complex

a = int(y)
b = float(x)
c = complex(x)

print(random.randrange(1, 10))

x = int(1) #1
y = int(2.8) #2
z = int("3") #3

x = float(1) #1.0
y = float(2.8) #2.8
z = float("3") #3.0
w = float("4.2") #4.2

x = str("s1") #"s1"
y = str(2) #"2"
z = str(3.0) #"3.0"

a = "Hello, World"
print(a[0])

for x in "banana":
    print(x + '\n')

a = "Hello, World"
print(len(a))

txt = "the best things in life are free"
print("free" in txt)
print("expensive" in txt)

b = "hello, world"
print(b[2:5])
print(b[:5])
print(b[-5:-2])




