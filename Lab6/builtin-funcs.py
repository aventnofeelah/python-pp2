import math
import time
#1
numbers = [1, 2, 3, 4, 5]
result = math.prod(numbers) 
print(result)

#2
string = "helloHELLO"
uc = 0
lc = 0
for x in string:
    if x.isupper():
        uc += 1
    else:
        lc += 1
print(f"Uppercase: {uc} Lowercase: {lc}")

#3
s = input("Input string: ")
if s == s[::-1]:
    print("Yes")
else:
    print("No")

#4
num = int(input("Enter a number: "))
ms = int(input("Enter a milliseconds: "))
time.sleep(ms / 1000)
print(math.sqrt(num))

#5
collection = (0, True, True)
print(all(collection))