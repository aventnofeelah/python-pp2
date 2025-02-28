import math

#1
deg = int(input("Input degree: "))
print(f"Output radian: {math.radians(deg)}")

#2
heg = int(input("Height: "))
base1 = int(input("Base, first value: "))
base2 = int(input("Base, second value: "))
print(f"Output: {(base1 + base2) / 2 * heg}")

#3
sides_num = int(input("Input number of sides: "))
side_len = int(input("Input the length of a side: "))
print(f"Output: {(sides_num * side_len**2 / 4) * (1 / math.tan(math.radians(180 / sides_num)))}")

#4
base_l = int(input("Length of base: "))
heg = int(input("Height of parallelogram: "))
print(base_l * heg)