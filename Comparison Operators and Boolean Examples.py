

# ------------------------------------------
# Comparison Operators and Boolean Examples
# ------------------------------------------

x = 10
y = 5

print("x == y:", x == y)    # False
print("x != y:", x != y)    # True
print("x > y:", x > y)      # True
print("x < y:", x < y)      # False
print("x >= y:", x >= y)    # True
print("x <= y:", x <= y)    # False
#!===========================================
# ------------------------------------------
# If, Else, and Elif (Conditional Statements)
# ------------------------------------------

x = 10
y = 5

# Simple if statement
if x > y:
    print("x is greater than y")  # This will run because 10 > 5
#!===========================================
# If...else example
x = 3
y = 5

if x > y:
    print("x is greater than y")
else:
    print("x is not greater than y")  # This will run because 3 < 5
#!================================================
# If...elif...else example
x = 5
y = 5

if x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")  # This will run because 5 == 5
else:
    print("x is less than y")
#!=========================================================
# ------------------------------------------
# Example: Checking if user can purchase item
# ------------------------------------------

balance = 500
price = 200

if balance >= price:
    print("Purchase successful. Remaining balance is", balance - price)
else:
    print("Insufficient balance. Please add funds to your account.")
#!============================================