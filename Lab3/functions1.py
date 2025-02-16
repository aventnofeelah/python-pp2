#1
def convertGrams(grams):
    return grams * 28.3495231
print(convertGrams())
#2
def convertTemp(far):
    return (5 / 9) * (far - 32)
print(convertTemp())
#3

#4
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def filter_prime(l1):
    primes = []
    for x in l1:
        c = 0
        for i in range(1, x + 1):
            if x % i == 0:
                c += 1
        if c <= 2:
            primes.append(x)
    return primes 
print(filter_prime(numbers))

#5

#6
def reverseStr():
    s = input("Enter string: ")
    return s[::-1]
print(reverseStr())

#7
numbers = [1, 2, 3, 4, 3, 4]
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            is_found = True
        else:
            is_found = False
    return is_found
print(has_33(numbers))

#8
numbers = [7, 0, 8, 0, 0, 6]
def spy_game(nums):
    cz = 0
    cs = 0
    is_found = False
    for i in range(len(numbers) - 2):
        if nums[i] == 0:
            cz += 1
        elif nums[i] == 7:
            cs += 1
    if cs == 1 and cz == 2:
        is_found = True
    return is_found
print(spy_game(numbers))

#10
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 1, 2, 3]
def find_unique(nums):
    uniques = []
    for i in range(len(nums)):
        c = 0
        for j in range(len(nums)):
            if nums[i] == nums[j]:
                c += 1
        if c == 1:
            uniques.append(nums[i])
    return uniques
print(find_unique(numbers))

#11
string = "hello"
def is_palindrome(word):
    is_palindrome = False
    if word == word[::-1]:
        is_palindrome = True
    return is_palindrome
print(is_palindrome(string))

12
numbers = [4, 5, 6]
def histogram(l1):
    for x in l1:
        print("*" * x)
histogram(numbers)

#13
import random
def guessGame():
    counter = 1
    user_num = -1
    num = random.randint(1, 20)
    name = str(input("Hello! What is your name? "))
    print("Well,", name, ", I am thinking of a number between 1 and 20.")
    while user_num != num:
        user_num = int(input("Take a guess "))
        if user_num > num:
            print("Your guess is too high.")
            counter += 1
        elif user_num < num:
            print("Your guess is too low.")
            counter += 1
        else:
            print("Good job, KBTU! You guessed my number in", counter, "guesses!")
guessGame()
        


    
