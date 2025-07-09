# 1. List Comprehensions with Conditions
# This builds a list of the squares of even numbers from 0 to 9.
squares = [x**2 for x in range(10) if x % 2 == 0]
print(squares)  # Output: [0, 4, 16, 36, 64]

# 2. Lambda Functions and map/filter
numbers = [1, 2, 3, 4, 5]
# map applies the lambda to each item, doubling each number
doubled = list(map(lambda x: x * 2, numbers))
# filter keeps only numbers that are even
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(doubled)  # Output: [2, 4, 6, 8, 10]
print(evens)    # Output: [2, 4]

# 3. Decorators
# Decorators let you wrap another function with extra behavior
def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@my_decorator  # This applies the decorator to say_hello
def say_hello():
    print("Hello!")

say_hello()
# Output: Before function
#         Hello!
#         After function

# 4. Generators and yield
# Generators use 'yield' to produce a series of values lazily
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for i in countdown(5):
    print(i)  # Prints 5, 4, 3, 2, 1

# 5. Context Managers (with statement)
# Context managers automate setup and cleanup (like opening/closing files)
class FileOpener:
    def __init__(self, filename):
        self.filename = filename
    def __enter__(self):
        self.file = open(self.filename, 'r')
        return self.file
    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

# Use the custom context manager to open and read a file
with FileOpener('example.txt') as f:
    content = f.read()
    print(content)

# 6. Multithreading
# Multithreading can run functions concurrently (not always in parallel due to GIL)
import threading

def worker(num):
    print(f"Worker {num}")

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()  # Each thread runs worker(i) concurrently

# 7. Using Classes and Inheritance
# Inheritance lets you extend classes. Dog overrides speak from Animal.
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Woof!")

dog = Dog()
dog.speak()  # Output: Woof!

# 8. Exception Handling
# try/except/finally helps you catch and respond to errors.
try:
    result = 10 / 0  # This will raise ZeroDivisionError
except ZeroDivisionError as e:
    print("Cannot divide by zero!")
finally:
    print("This always runs")