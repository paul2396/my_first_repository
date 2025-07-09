# ================================
# 🌀 Range and Loop Examples
# ================================

# 1. For loop that prints only even numbers from 0 to 10
for i in range(11):
    if i % 2 != 0:
        continue  # Skip odd numbers
    print(i)

# ===========================================
# 2. For loop using range in reverse (from 10 to 0)
for i in range(10, -1, -1):
    print(i)  # Prints numbers 10 to 0 in reverse order

# ===========================================
# 3. For loop with a step size of 3 (prints every 3rd number)
for i in range(0, 60, 3):
    print(i)

# ===========================================
# 4. Using range() to build a list of numbers from 62 to 230
numbers = list(range(62, 230))
print("List of numbers from 62 to 230:", numbers)

# ===========================================
# 5. For loop using range with characters (A to Z)
for i in range(ord('A'), ord('Z') + 1):
    print(chr(i))  # Converts ASCII to character

# ===========================================
# Global keyword example
x = 'awesome'

def myfunc():
    global x
    x = 'fantastic'

myfunc()
print('Python is ' + x)

# ===========================================
# Check if user can purchase a product
balance = 500
price = 200

if balance >= price:
    print("Purchase successful. Remaining balance is", balance - price)
else:
    print("Insufficient balance. Please add funds to your account.")

# ===========================================
# Math operations and type casting
a = 5
b = 2
print(a // b)  # Floor division

value = 2 + 3 * 4 / 2
print(value)  # Follows operator precedence

num = "8"
result = int(num) + 5
print(result)

str = "GFG"
print(not (not(str and "")))  # Logical evaluation

print(oct(23) + oct(23))  # Concatenates octal strings

print(~(~2))  # Double bitwise NOT returns original

# ===========================================
# Range loop examples
print("Range from 0 to 4:")
for i in range(5):
    print(i)

print("\nRange from 2 to 6:")
for i in range(2, 7):
    print(i)

print("\nRange with step of 14:")
for i in range(0, 100, 14):
    print(i)

print("\nRange in reverse order:")
for i in range(10, 0, -2):
    print(i)

print("\nConverting range to a list:")
numbers = list(range(5, 15))
print(numbers)

# NOTE: below is my list of loop types
# 1. for loop
# 2. while loop
# 3. do-while loop (simulated in Python)

# ===========================================
# List of days in a week
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Loop through the list and print each day
for day in days:
    print(day)

# Loop through the list with enumerate to get index and value
for index, day in enumerate(days):
    print("days[{0}] contains {1}".format(index, day))
    print("day contains {0}".format(day))

# Loop with enumerate, human-friendly numbering (1-based)
for index, day in enumerate(days):
    print("{0} is day # {1}".format(day, index + 1))

# ===========================================
# While loop that prints numbers 1 to 5
print("While loop 1 to 5:")
count = 1
while count <= 5:
    print(count)
    count += 1

# While loop that breaks when condition is met
print("\nWhile loop with break:")
num = 0
while True:
    num += 1
    print(num)
    if num >= 3:
        break

# Simulated do-while loop in Python (runs at least once)
print("\nSimulated do-while loop:")
x = 0
while True:
    print("x is:", x)
    x += 1
    if x >= 1:
        break

# ===========================================
# Simple list printing
lis1 = [300, 89, 4, 300, 23, 89, 200, 76]
print(lis1)
#!============================================
# ================================
# ✅ If / Elif / Else Examples
# ================================

# ➤ Simple if statement
age = 20
if age >= 18:
    print("You are an adult.")  # This will print because age is 20

# ➤ If...else statement
temperature = 12
if temperature > 15:
    print("It's warm outside.")
else:
    print("It's a bit chilly.")  # This will print

# ➤ If...elif...else ladder
score = 75

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")  # This will print because score is 75
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# ➤ Checking multiple conditions
name = "Paul"
age = 79

if name == "Paul" and age >= 60:
    print("Welcome, retired legend!")  # This will print

# ➤ Nested if statements
weather = "rainy"
have_umbrella = True

if weather == "rainy":
    if have_umbrella:
        print("You can go out with your umbrella.")  # This will print
    else:
        print("Better stay indoors.")
else:
    print("Enjoy your day!")

# ➤ Using not operator
is_sunny = False

if not is_sunny:
    print("It's not sunny today.")  # This will print

# ➤ Short if (ternary expression)
age = 17
message = "You can vote." if age >= 18 else "You are too young to vote."
print(message)  # Prints: You are too young to vote.
