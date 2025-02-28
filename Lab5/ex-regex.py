import re

with open('C:\Code\python-files\python-univ\Lab5\products.txt', "r", encoding='utf-8') as file:
    lines = file.read().splitlines()

#1
for x in lines:
    if re.findall("a*b", x):
        print(x)

#2
for x in lines:
    if re.findall("ab{2,3}", x):
        print(x)

#3
for x in lines:
    if re.findall("[a-z]+_[a-z]+", x):
        print(x)

#4
for x in lines:
    if re.findall("[A-Z]+[a-z]+", x):
        print(x)

#5
for x in lines:
    if re.findall("^a.b$", x):
        print(x)

#6
with open('C:/Code/python-files/python-univ/Lab5/new-products.txt', "w", encoding='utf-8') as new_file:
    for x in lines:
        temp = ""
        for j in x:
            if j != " " and j != "." and j != ",":
                temp += j
        new_file.write(temp + "\n")
            
#7
def replaceFunc(match):
    print(match.group(0))
    return match.group(1).upper()
snake = input("Enter string in snake case: ")
camel = re.sub("_([a-z])", replaceFunc, snake)
print(camel)

#8
def replaceFunc(match):
    print(match.group())
    return match.group(1) + " " + match.group(2)
s = "HelloBraveNewWorld"
new_s = re.sub("([a-z])([A-Z])", replaceFunc, s)
print(new_s)

#10
def replaceFunc(match):
    return match.group(1) + "_" + match.group(2).lower()
camel = input("Enter string in camel case: ")
snake = re.sub("([a-z])([A-Z])", replaceFunc, camel)
print(snake)

        
                