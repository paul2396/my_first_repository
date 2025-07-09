# ============================
# 🔁 Looping with range() and len()
# ============================

# ➤ Loop through a list using range() and len()
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])  # Prints the index and the corresponding word

# ➤ Loop through another list using range() and len()
w = ["neverending", "transgress", "nevertheless"]
for i in range(len(w)):
    print(w[i])  # Prints each word from the list

# ============================
# 🔁 break and continue Statements
# ============================

# ➤ break: Find factors and stop at the first one
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n // x}")  # Shows the factor pair
            break  # Exit the inner loop once a factor is found

# ➤ continue: Skip even numbers
for num in range(2, 10):
    if num % 2 == 0:
        print(f"Found an even number {num}")
        continue  # Skip the rest and go to next number
    print(f"Found an odd number {num}")

# ============================
# 🔍 else Clauses on Loops (Prime Check)
# ============================

# ➤ Check for prime numbers using for-else
for n in range(2, 30):
    for x in range(2, n):
        if n % x == 0:
            print(n, "equals", x, "*", n // x)
            break
    else:
        print(n, "is a prime number")  # Only prints if the loop wasn't broken

# ============================
# ⚖️ Filtering with Lambda and filter()
# ============================

# ➤ Filter numbers divisible by 10
my_list = [17, 34, 51, 40, 68, 70, 119, 327, 243, 900, 400, 700, 56, 200, 89, 67, 40]
result = list(filter(lambda x: (x % 10 == 0), my_list))
print("Numbers divisible by 10 are", result)

# ➤ Filter numbers divisible by 3 and 12
div_by_3 = list(filter(lambda x: x % 3 == 0, my_list))
div_by_12 = list(filter(lambda x: x % 12 == 0, my_list))
print("Divisible by 3:", div_by_3)
print("Divisible by 12:", div_by_12)

# ============================
# 🧠 match Statement Example
# ============================

# ➤ Match HTTP status codes using Python 3.10+ match-case
def http_error(status):
    match status:
        case 400:
            return "Bad Request"
        case 404:
            return "Not Found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

status_code = 404
result = http_error(status_code)
print(result)

# ============================
# 🧾 Docstring Example
# ============================

# ➤ Multi-line docstring in a function
def my_function():
    """Do nothing but document it.
    No really, it doesn't do anything."""
    pass

print(my_function.__doc__)  # Prints the function's docstring

# ============================
# 👴 Age Checker Logic
# ============================

# ➤ Categorize age ranges with if/elif/else
age = 105

if age > 120:
    print("How are you even alive?")
elif age > 100:
    print("You're old")
else:
    print("You may have some years left in you")

# ➤ Another version of age check
if age > 50:
    print("You are not that old")
elif 45 < age <= 50:
    print("You are not old")
else:
    print("You may have some years left in you")

# ============================
# 🔤 String: Sort Words Alphabetically
# ============================

# ➤ Sort and print words in a sentence
my_str = "The quick brown fox jumps over the lazy dog"
words = [word.lower() for word in my_str.split()]
words.sort()

print("The sorted words are:")
for word in words:
    print(word)

# ============================
# 🔢 Armstrong Number Finder
# ============================

# ➤ Function to find Armstrong numbers in a given range
def find_armstrong_numbers(lower, upper):
    """Prints Armstrong numbers between lower and upper limits."""
    for num in range(lower, upper + 1):
        num_digits = len(str(num))
        total = 0
        temp = num
        while temp > 0:
            digit = temp % 10
            total += digit ** num_digits
            temp //= 10
        if num == total:
            print(num)  # Print only if it's an Armstrong number

# Example usage
find_armstrong_numbers(10, 500)

# ============================
# ➕ Matrix Addition Example
# ============================

X = [[12, 9, 3],
     [4, 5, 6],
     [7, 8, 3]]

Y = [[9, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]

result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

# ➤ Add corresponding elements from both matrices
for i in range(len(X)):
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]

for r in result:
    print(r)

# ============================
# ➰ More Range Examples
# ============================

print("Range from 0 to 4:")
for i in range(5):
    print(i)

print("\\nRange from 2 to 6:")
for i in range(2, 7):
    print(i)

print("\\nRange with step of 10:")
for i in range(0, 100, 10):
    print(i)

print("\\nRange in reverse order (count down by 5):")
for i in range(100, 0, -5):
    print(i)

print("\\nConverting range to a list:")
numbers = list(range(5, 15))
print(numbers)

