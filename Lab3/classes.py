import math
#1
class ShowString():
    def getString(self):
        global s
        s = input("Enter string: \n")
    def printString(self):
        return s.upper()
obj = ShowString()
obj.getString()
print(obj.printString())

#2, 3
class Shape():
    def __init__(self, length = 0):
        self.length = length
    def area(self):
        return self.length
class Square(Shape):
    def area(self):
        return self.length
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def comp_area(self):
        return f"Area: {self.length * self.width}"
obj1 = Shape()
obj2 = Square(6)
obj3 = Rectangle(5, 5)
print(obj1.area())
print(obj2.area())
print(obj3.comp_area())


#4
class Point():
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    def show(self):
       return f"X1: {self.x1}, Y1: {self.y1}\nX2: {self.x2}, Y2: {self.y2}" 
    def move(self):
        print("Current coordinates:", "\n", "X1:", self.x1, "Y1:", self.y1, "\n", "X2:", self.x2, "Y2:", self.y2)
        new_x1 = int(input("Enter new X1 coordinate: \n"))
        new_y1 = int(input("Enter new Y1 coordinate: \n"))
        new_x2 = int(input("Enter new X2 coordinate: \n"))
        new_y2 = int(input("Enter new Y2 coordinate: \n"))
        self.x1 = new_x1
        self.y1 = new_y1
        self.x2 = new_x2
        self.y2 = new_y2
        return f"X1: {self.x1}, Y1: {self.y1}\nX2: {self.x2}, Y2: {self.y2}" 
    def dist(self):
        return math.sqrt((self.x2 - self.x1)**2 + (self.y2 - self.y1))
obj1 = Point(2, 2, 5, 5)
print(obj1.show())
print(obj1.move())
print(obj1.dist())

#5
class Account():
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
    def deposit(self):
        print("Hello, ", self.owner)
        print("Current balance: ", self.balance)
        dep = int(input("Enter the amount you want to deposit: "))
        self.balance += dep
        print("Current balance: ", self.balance)
    def withdraw(self):
        print("Hello, ", self.owner)
        print("Current balance: ", self.balance)
        while True:
            wd = int(input("Enter the amount you want to withdraw: "))
            if(wd > self.balance):
                print("Sorry, not enough funds\n")
            else:
                self.balance -= wd
                break
        print("Current balance: ", self.balance,"\n")
obj1 = Account("John", 10000)
obj1.deposit()
obj1.withdraw()

#6
 

