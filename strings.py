# ================================
# 🧵 Python String Examples
# ================================

# Note: Python strings are immutable — you can't change them in place.

# ➤ Strings can be enclosed in single quotes
print('Hello World in single quotes')

# ➤ Strings can also be enclosed in double quotes
print("Hello World in double quotes")

# ➤ Strings can also be enclosed in triple quotes
print("""This is a multiline string.
These strings can contain 'single' as well as "double" quotes.""")

# ➤ Strings continued on the next line (no actual newline added)
print("This string is continued on the\
next line (in the source) but a newline is not added")

# ➤ Raw strings (useful for file paths and regular expressions)
print(r"The newline character is represented with \n")

# ➤ Unicode string
print(u"This is a unicode string: \u0600")  # \u0600 is a Unicode character

# ➤ String concatenation
print('hello ' 'world')  # Concatenated at compile time

# ➤ Comma-separated values in print() add spaces automatically
print('2 + 3 =', (2 + 3))

# ➤ Getting the length of a string
greeting = "Hello my dear friend how are you?"
print("The length of string '" + greeting + "' is " + str(len(greeting)))

# ➤ Check if a word exists in a string
if 'Hello' in greeting:
    print("This greeting seems to be in English")

# ➤ Using find() to locate a substring (returns index or -1)
if greeting.find('Hello') != -1:
    print("This greeting seems to be in English")

# ================================
# ✂️ String Slicing
# ================================

text = "Python is powerful"

print("First 6 characters:", text[:6])         # Python
print("Last 8 characters:", text[-8:])         # powerful
print("Middle slice:", text[7:9])              # is
print("Every second letter:", text[::2])       # Pto spoefu

# ================================
# 🔤 Useful String Methods
# ================================

sample = "  Hello, Paul! Welcome to Python.  "

print("Uppercase:", sample.upper())            # Converts to uppercase
print("Lowercase:", sample.lower())            # Converts to lowercase
print("Stripped:", sample.strip())             # Removes leading/trailing spaces
print("Title Case:", sample.title())           # Capitalizes each word
print("Replaced:", sample.replace("Paul", "Ted"))  # Replace a word
print("Starts with Hello:", sample.startswith("Hello"))  # False due to space
print("Ends with .:", sample.endswith("."))    # False due to trailing space

# ================================
# 🧮 Split, Join, and Count
# ================================

line = "apple,banana,cherry"

fruits = line.split(",")  # Splits string into list
print("Fruits list:", fruits)

joined = " - ".join(fruits)  # Joins list back into string
print("Joined fruits:", joined)

count = line.count("a")
print("Number of 'a's in line:", count)

# ================================
# 🧵 String Formatting
# ================================

name = "Paul"
age = 79

# f-strings (Python 3.6+)
print(f"My name is {name} and I am {age} years old.")

# str.format()
print("My name is {} and I am {} years old.".format(name, age))

# Old style formatting
print("My name is %s and I am %d years old." % (name, age))

# Padding and alignment
print(f"|{'left':<10}|{'center':^10}|{'right':>10}|")

# ================================
# 🔍 Checking and Validating Strings
# ================================

email = "paul@example.com"

if email.endswith("@example.com"):
    print("Email is from example.com")

if email.islower():
    print("Email is all lowercase")

if email.isalnum():
    print("Email has only letters and numbers (False in this case)")

# ================================
# 🧪 Testing and Comparison
# ================================

word = "Python"
if word.lower() == "python":
    print("Case-insensitive match")

# Check if input is a digit
user_input = "12345"
if user_input.isdigit():
    print("Input is a number")

# Check if string is alphabetic
if "Hello".isalpha():
    print("Only letters in string")

# Check if string is alphanumeric
if "abc123".isalnum():
    print("String contains letters and numbers")

# ================================
# 🧹 Bonus: Remove punctuation from string
# ================================

import string

messy = "Hello!!! This, right here, is a messy sentence... :)"
clean = "".join(char for char in messy if char not in string.punctuation)
print("Cleaned sentence:", clean)
mylist