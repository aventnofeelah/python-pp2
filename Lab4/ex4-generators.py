#1
def square_gen(n):
    c = 0
    while c != n:
        c+=1
        yield c**2
        
gen = square_gen(5)
for x in gen:
    print(x)

#2
number = int(input("Enter number: "))
def even_nums(n):
    for i in range(n):
        if i % 2 == 0:
            yield i
gen = even_nums(number)
for x in gen:
    print(x, end=", ")

#3
def iter_nums(n):
    for i in range(n):
        if i % 3 == 0 and i % 4 == 0:
            yield i
gen = iter_nums(25)
for x in gen:
    print(x)

#4
def squares(a, b):
    for i in range(a, b):
        yield i**2
gen = squares(5, 10)
for x in gen:
    print(x)

#5
def gen5(n):
    for i in range(n, 0, -1):
        yield i
gen = gen5(5)
for x in gen:
    print(x)