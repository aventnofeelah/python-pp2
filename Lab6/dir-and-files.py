import os
#1
src = "C:\Code\python-files\python-univ"
files = []
dirs = []
for x in os.listdir(src):
    if os.path.isfile(x):
        files.append(x)
    elif os.path.isdir(x):
        dirs.append(x)
print(f"FILES: {files}")
print(f"DIRS: {dirs}")

#2
src = "C://Code//python-files//python-univ//Lab6//test.txt"
if os.path.exists(src):
    print("Path exists")
    print(f"Readability: {os.access(src, os.R_OK)}")
    print(f"Writeability: {os.access(src, os.W_OK)}")
    print(f"Executability: {os.access(src, os.X_OK)}")
else:
    print("Path does not exists")

#3
src = "C://Code//python-files//python-univ//Lab6//test.txt"
if os.path.exists(src):
    if os.path.isfile(src):
        print(f"Type: file. Name: {os.path.basename(src)}")
    else:
        print(f"Type: directory. Name: {os.path.basename(src)}")
else:
    print("Path does not exits")

#4
src = "C://Code//python-files//python-univ//Lab6//test.txt"
if os.path.isfile(src):
    root, ext = os.path.splitext(src)
    if ext != '.txt':
        print("File is not a txt file")
    else:
        with open(src, 'r', encoding="utf-8") as file:
            print(f"Number of strings: {len(file.readlines())}")
else:
    print("Input path to a file")

#5
nums = [1, 2, 3, 4, 5, 6]
str_list = ""
for x in nums:
    str_list += str(x) + ' '
src = "C://Code//python-files//python-univ//Lab6//test.txt"
with open(src, 'a', encoding="utf-8") as file:
    file.write(str_list + "\n")

#6
alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
src = "C://Code//python-files//python-univ//Lab6"
for x in alph:
    temp = src + "//" + x + '.txt'
    with open(temp, 'w', encoding="utf-8") as file:
        pass

#7
src = "C://Code//python-files//python-univ//Lab6//test.txt"
with open(src, "r", encoding="utf-8") as file:
    data = file.readlines()
with open("C://Code//python-files//python-univ//Lab6//copy.txt", "w", encoding="utf-8") as new_file:
    for x in data:
        new_file.write(x)

#8
src = "C://Code//python-files//python-univ//Lab6//file-for-deletion.txt"
if os.path.exists(src) and os.access(src, os.R_OK):
    os.remove(src)
else:
    print("File does not exists or access denied")