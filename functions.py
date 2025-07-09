# =============================
# 👋 Greeting & Introduction Functions
# =============================

# ➤ Meet someone by name, job title, and city
def meet(name, job_title, city):
    return f"Meet {name}, a {job_title} from {city}."

# Example usage

meet2 = meet('John', 'Artist', 'Austin')  # Shows standard positional use
meet3 = meet(city='Madison', name='Ashley', job_title='Developer')  # Keyword arguments (order doesn't matter)

print(meet1)
print(meet2)
print(meet3)

# ➤ Friendly hello function
def hello(name, job_title, country, city):
    return f"Hi {name}, I hear you're a {job_title} from {country} and you live in {city}."

# Example usage
hello1 = hello('Fred', 'bricklayer',"England", 'London')
hello2 = hello("Sam", "joiner", "Scotland","Glasgow"
hello3 = hello("Ted", "flagger", "Wales", "Cardiff")
hello4 = hello("Jill", "hairdresser", "Ireland", "Belfast")

print(hello2)
print(hello3)

# =============================
# 🔍 Info & Doc Examples
# =============================
#How do I create a list in Python?

# ➤ Use help() to explore built-in topics
help("functions")  # Opens Python help documentation on functions

# =============================
# 🔢 Number Functions
# =============================

# ➤ Check if a number is prime
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):  # Only check up to sqrt of number
        if number % i == 0:
            return False
    return True

print(is_prime(7))    # ✅ True
print(is_prime(10))   # ❌ False

# ➤ Get age using assert to prevent negative numbers
def get_age(age):
    assert age >= 0, "Age cannot be negative"
    print("Your age is:", age)

get_age(30)
# get_age(-1)  # ❌ Uncommenting this will raise an AssertionError

# ➤ Average of a list of numbers
def avg_list(numbers, total=0):
    assert len(numbers) > 0, "List cannot be empty"
    for num in numbers:
        total += num
    average = total / len(numbers)
    print("Average is:", average)

avg_list([1, 2, 3, 4])
# avg_list([])  # ❌ Raises an error: empty list

# =============================
# 👽 Alien Species Name Generator
# =============================

import random

# ➤ Generate a random alien species name
def generate_alien_name():
    prefixes = ["Zor", "Xan", "Vel", "Kra", "Tor", "Lun", "Mor"]
    middles = ["quar", "zen", "lax", "thar", "bex", "ruk"]
    suffixes = ["oid", "an", "ite", "ari", "ax", "ulon"]
    return random.choice(prefixes) + random.choice(middles) + random.choice(suffixes)

print("Your alien species name is:", generate_alien_name())

# =============================
# 🆕 Bonus Function Ideas (Optional)
# =============================

def c_to_f(celsius):
    return (celsius * 9/5) + 32  # Convert to Fahrenheit

print("20°C is", c_to_f(20), "°F")

def reverse_string(text):
    return text[::-1]  # Reverses a string

print("Reversed word of 'Python' is", reverse_string("Python"))

#!=======================================
# Function assigned to a variable
def func(x, y):
    return x + y

print(type(func))  # Shows it's a function <class 'function'>

# Function aliasing
show = print
show("something")  # Calls print using alias

# Using enumerate to loop with index
name = ["jatin", "gt", "afreed", "shiva", "guru"]
for item in enumerate(name):
    print(item)  # Prints (index, value)

#!=============================================
# Function with mood-based response
def maxie(mood):
    mood = mood.lower()  # Makes input case-insensitive
    if mood == "happy":
        return "You are happy! 😊"
    elif mood == "sad":
        return "You are sad. 😢"
    elif mood == "excited":
        return "You're full of excitement! 🎉"
    elif mood == "angry":
        return "Take a breath, you're feeling angry. 😠"
    elif mood == "tired":
        return "Sounds like you need some rest. 😴"
    else:
        return "Mood not recognized! 🤔"

print(maxie("Excited"))
print(maxie("TIRED"))
print(maxie("angry"))

#!====================================================
sentence = "Python is a versatile language."
sentence.split()  # Splits into list of words

text="""line one
line two
line three"""
text.split()  # Splits into list by spaces

#!============================================
letters = ["a", "b", "c", "d", "e"]
print(letters[:3])  # Slice: first 3 letters

#!============================================
# Function with parameters
def greet(name):
    print("Hello,", name)

greet("Paul")

# Function with return value
def multiply(a, b):
    return a * b

result = multiply(3, 4)
print("3 multiplied by 4 is", result)

# Function with default parameter
def welcome(name="guest"):
    print("Welcome,", name)

welcome()
welcome("Ted")

# Lambda function example
square = lambda x: x * x
print("Square of 5 is", square(5))

# Function redefinition (OK, but replaces previous one)
def greet(name):
    print("Hello,", name)

greet("Alice")

#!==========================================
# Extended greet function with more detail
def greet(name, job_title, city, country, hobby):
    return f"Meet {name}, a {job_title} from {country} living in {city} who enjoys {hobby}."

# Main function to run multiple greetings
def main():
    greet1 = greet('Tom', 'Joiner', 'Bristol', 'UK', 'reading')
    greet2 = greet('Fred', 'Electrician', 'Glasgow', 'UK', 'cycling')
    greet3 = greet('Fred', 'Electrician', 'York', 'UK', 'hiking')
    greet4 = greet('June', 'Hairdresser', 'Belfast', 'Ireland', 'painting')

    print(greet1)
    print(greet2)
    print(greet3)
    print(greet4)

if __name__ == "__main__":
    main()  # Ensures code only runs when script is executed directly

x = 10
y = 5
result = x > y  # Boolean comparison
print(result)
#!=================================================
# Example 1: 

# Take a list of numbers
my_list = [17, 34, 51, 43, 68, 72, 119, 327, 243, 986]

# use anonymous function to filter
result = list(filter(lambda x: (x % 21 == 0), my_list))# you can change the == to any number

# display the result
print("Numbers divisible by 3 are", result)
#!=============================================
def goodbye(name):
    return f"Goodbye, {name}! See you soon, {name}. See you later, {name}. Maybe next time, {name}."

print(goodbye("Paul"))
print(goodbye("Ted"))
print(goodbye("Ashley"))
print(goodbye("June"))
print(goodbye("Fred"))
#!=============================================
def favorite_color(color):
    return f"Hi! is Your favorite color {color}!"

print(favorite_color("blue"))
print(favorite_color("green"))
print(favorite_color("red"))
#!=====================================
def favorite_things(name, color, animal, hobby):
    return f"Hi!{name} Your favorite color is {color} and your favorite animal is a {animal} and your hobby is? {hobby}"

print(favorite_things("Ted","blue", "dog", "reading"))
print(favorite_things("Bill","green", "cat", "painting"))
print(favorite_things("june","red", "parrot", "cycling"))# i can add amost any number of things to the function and it will work
print(favorite_things("Paul","yellow", "fish", "hiking"))
#!=====================================================

# 👋 Greeting & Introduction Functions
# =============================

# ➤ Meet someone by name, job title, and city
def meet(name, job_title, city):
    return f"Meet {name}, a {job_title} from {city}."

# Example usage
meet1 = meet('Fred', 'bricklayer', 'London')
meet2 = meet('John', 'Artist', 'Austin')  # Corrected argument order
meet3 = meet(city='Madison', name='Ashley', job_title='Developer')

print(meet1)
print(meet2)
print(meet3)

# ➤ Friendly hello function
def hello(name, job_title, country, city):
    # Corrected the function to include 'country' and 'city'
    return f"Hi {name}, I hear you're a {job_title} from {country} and you live in {city}."

# Example usage
hello1 = hello('Fred', 'bricklayer', 'England', 'London')
hello2 = hello("Sam", "joiner", "Bristol")
hello3 = hello("Ted", "flagger", "Manchester")
hello4 = hello("Jill", "hairdresser", "Exeter")

print(hello1)
print(hello2)
print(hello3)

# 🔢 Number Functions
# =============================

# ➤ Check if a number is prime
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Example usage
print(is_prime(7))    # ✅ True
print(is_prime(10))   # ❌ False

# ➤ Get age using assert to prevent negative numbers
def get_age(age):
    assert age >= 0, "Age cannot be negative"
    print("Your age is:", age)

# Example usage
get_age(30)
# get_age(-1)  # ❌ Uncommenting this will raise an AssertionError

# ➤ Average of a list of numbers
def avg_list(numbers, total=0):
    assert len(numbers) > 0, "List cannot be empty"
    for num in numbers:
        total += num
    average = total / len(numbers)
    print("Average is:", average)

# Example usage
avg_list([1, 2, 3, 4])
# avg_list([])  # ❌ Uncommenting this will raise an AssertionError

# =============================
# 👽 Alien Species Name Generator
# =============================

import random

# ➤ Generate a random alien species name
def generate_alien_name():
    prefixes = ["Zor", "Xan", "Vel", "Kra", "Tor", "Lun", "Mor"]
    middles = ["quar", "zen", "lax", "thar", "bex", "ruk"]
    suffixes = ["oid", "an", "ite", "ari", "ax", "ulon"]
    return random.choice(prefixes) + random.choice(middles) + random.choice(suffixes)

# Example usage
print("Your alien species name is:", generate_alien_name())

# =============================
# 🆕 Bonus Function Ideas (Optional)
# =============================

# ➤ Convert temperature from Celsius to Fahrenheit
def c_to_f(celsius):
    return (celsius * 9/5) + 32

print("20°C is", c_to_f(20), "°F")

# ➤ Reverse any string
def reverse_string(text):
    return text[::-1]

print("Reversed word of 'Python' is", reverse_string("Python"))

#!=======================================
def func(x, y):
    return x + y

print(type(func))

show = print
show("something")

name = ["jatin", "gt", "afreed", "shiva", "guru"]
for item in enumerate(name):
    print(item)
#!=============================================
def maxie(mood):
    mood = mood.lower()  # makes input case-insensitive
    
    if mood == "happy":
        return "You are happy! 😊"
    elif mood == "sad":
        return "You are sad. 😢"
    elif mood == "excited":
        return "You're full of excitement! 🎉"
    elif mood == "angry":
        return "Take a breath, you're feeling angry. 😠"
    elif mood == "tired":
        return "Sounds like you need some rest. 😴"
    else:
        return "Mood not recognized! 🤔"
print(maxie("Excited"))    # You're full of excitement! 🎉
print(maxie("TIRED"))      # Sounds like you need some rest. 😴
print(maxie("angry"))      # Take a breath, you're feeling angry. 😠
#!====================================================
sentence = "Python is a versatile language."
sentence.split()
text="""line one
line two
line three"""
text.split()
#!============================================
letters = ["a", "b", "c", "d", "e"]
print(letters[:3])
#!============================================
# Function with parameters
def greet(name):
    print("Hello,", name)

greet("Paul")

# Function with return value
def multiply(a, b):
    return a * b

result = multiply(3, 4)
print("3 multiplied by 4 is", result)

# Function with default parameter
def welcome(name="guest"):
    print("Welcome,", name)

welcome()
welcome("Ted")

# Lambda function example
square = lambda x: x * x
print("Square of 5 is", square(5))
# Function with parameters
def greet(name):
    print("Hello,", name)

greet("Paul")

# Function with return value
def multiply(a, b):
    return a * b

result = multiply(3, 4)
print("3 multiplied by 4 is", result)

# Function with default parameter
def welcome(name="guest"):
    print("Welcome,", name)

welcome()
welcome("Ted")

# Lambda function example
square = lambda x: x * x
print("Square of 5 is", square(5))
#!===================================================
# Call the function to execute the code
# new_func()
users={"billy":"active","Tomy":"inactive","Siade":"just_about"}
for user, status in users. copy().items():
    if status=="inactive": del users[user]
    print(users)
    
    # Strategy:  Create a new collection
    active_users={}
    for user, status in users.items():
     if status =="active==":
        active_users[user]=status
        print(active_users)
        
#!========================================
#!The range() Function¶
#!To iterate over the indices of a sequence,
# you can combine range() and len() as follows
w = ["neverending", "transgrees", "nevertheless"]

for i in range(len(w)):
    print(w[i])
#!=============================================
#!break and continue Statements, and else Clauses on Loops
for n in range(2,30):
    for x in range(2, n):
        if n % x ==0:
            print(n,"equals",x,"*",n//x)
            break
    else:
        print(n, "Is a prime number")

#1=================================================

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
#!=====================================================
#!The continue statement, also borrowed from C,
# continues with the next iteration of the loop:
for num in range(2,10):
    if num % 2 == 0:
          print("found an even number",num)
          continue
    print("found an odd number",num)
#!=================================================
#!The simplest form compares a subject value
# against one or more literals:
def http_error(status):
    match status:
        case 400:
            return"bad request"
        case 404:
            return"not found"
        case 418:
            return "i'am a tea pot"
        case _:
            return"something wrong with the internet"
status_code = 404
result = http_error(status_code)
print(result)
#!====================================================================
#!Here is an example of a multi-line docstring:
def my_function():
    """do nothing but document i
    No realy it dosen't do anything"""
    pass
print(my_function.__doc__)
#!====================================================================
my_list = [1, 2, 3, 4, 5]
new_list = []
for it in my_list:
    new_list.append(it + 10)
print(new_list)
#!===========================================
numbers = [2, 7, 5, 4, 8]  # The code is a good example of how to use the built-in functions
# Example usage of len(), min(), max(), and sum() functions:
print(len(numbers))
print(min(numbers))
print(max(numbers))
print(sum(numbers))
#!========================================
# Example 1: sort alphabetically the words form a string provided by the user

my_str = "The quick brown fox jumps over the lazy dog"

# To take input from the user
#my_str = input("Enter a string: ")

# breakdown the string into a list of words
words = [word.lower() for word in my_str.split()]

# sort the list
words.sort()

# display the sorted words

print("The sorted words are:")
for word in words:
    print(word)
#!====================================================
def goodbye(name):
    print("Goodbye,", name)
    print("See you soon!")
    print("Take care!")
    print("Have a great day!")
#!======================================================
def favorite_color(color):
    print("Your favorite color is", color)
    print("That's a nice choice!")
    print("Colors can be so beautiful.")
    print("I love the way colors make us feel!")
    print("What other colors do you like?")
#!==========================================
def greet(name, country, city, interest1, interest2):
    print(f"Hi {name}, are you from {country}, do you live in {city}, and do you enjoy {interest1} and {interest2}?")

greet("Paul", "England", "Lancaster", "hill walking", "reading")
greet("Ted", "USA", "Austin", "bird watching", "swimming")
greet("Ashley", "Canada", "Toronto", "hiking", "reading")
greet("June", "Ireland", "Belfast", "swimming", "cycling")
greet("Fred", "Scotland", "Glasgow", "fishing", "hiking")
greet("Bill", "Wales", "Cardiff", "bird watching", "wood working")
#!=============================================================
#1. Function to check if a word is a palindrome
def is_palindrome(word):
    return word == word[::-1]

print(is_palindrome("level"))   # True
print(is_palindrome("python"))  # False
#!=============================================================
#2. Function to count vowels in a string.  
def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

print(count_vowels("Hello World"))  # 3
print(count_vowels("Programming"))  # 4
#!=============================================================
#3. Function to count the number of words in a string
def max_of_three(a, b, c):
    return max(a, b, c)

print(max_of_three(5, 12, 7,67,900,))  # 12
#!==============================================