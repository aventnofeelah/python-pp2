print(10 > 9)
print(10 == 9)
print(10 < 9)

print(bool("Hello")) #True
print(bool(15)) #True
bool(["apple", "cherry", "banana"]) #True

bool(False) #False
bool(None) #False
bool(0) #False
bool("") #False
bool(()) #False
bool([]) #False
bool({}) #False

x = 200
print(isinstance(x, int)) #True

print(10 + 5)
print(1 - 0)
print(5 * 4)
print(36 / 6)
print(101 % 10)
print(3**2)
print(89 // 9)

mylist = ["apple", "banana", "cherry"]
list_int = [1, 5, 7, 9, 3]
list_bool = [True, False, False]
list_any = ["abc", 34, True, 40, "male"]
print(mylist)
print(len(mylist))
print(type(mylist))

print(mylist[0]) #apple
print(mylist[-1]) #cherry
print(list_any[1:2])
print(list_any[2])
if "apple" in mylist:
  print("Yes, 'apple' is in the fruits list")

mylist[1] = "orange" #["apple", "orange", "cherry"]
mylist.insert(2, "watermelon") #["apple", "orange", "watermelon", "cherry"]
mylist.append("mango") #["apple", "orange", "watermelon", "cherry", "mango"]
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2) #list1 = [1, 2, 3, 4, 5, 6]

list_words = ["car", "computer", "doctor"]
list_words.remove("car") #["computer", "doctor"]
list_words.pop(0) #["doctor"]
list_words.pop() #removes last element
list_words = ["car", "computer", "doctor"]
list_words.clear() #[]
del list_words #deletes whole list

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
for i in range(len(thislist)):
  print(thislist[i])

#syntax newlist = [expression for item in iterable if condition == True]
newlist = [x for x in thislist if x != "apple"]
newlist = [x for x in thislist]

fruits = ["orange", "mango", "kiwi", "pineapple", "banana"]
fruits.sort() #alphabet order
thislist.sort(reverse = True) #reverse alphabet order
print(fruits)

new_fruits = fruits.copy() #["orange", "mango", "kiwi", "pineapple", "banana"]
new_fruit = fruits[:] #["orange", "mango", "kiwi", "pineapple", "banana"]

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2 #["a", "b", "c", 1, 2, 3]
list1.extend(list2) #["a", "b", "c", 1, 2, 3]

thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(len(thistuple))
print(type(thistuple))
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

print(thistuple[1]) #banana
print(thistuple[-1]) #cherry

#change element
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
#add elem
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
#del elem
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green) #apple
print(tropic) #["mango", "papaya", "pineapple"]
print(red) #cherry

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(thisdict["brand"])
print(len(thisdict))
print(type(thisdict))
x = thisdict.get("model")
x = thisdict.keys()
x = thisdict.values()
x = thisdict.items()
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
thisdict.update({"year": 2020})
thisdict["color"] = "red"
thisdict.pop("model")

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

c = 2
d = 330
print("A") if c > d else print("B")

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)