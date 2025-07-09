# ================================
# 📁 File Handling in Python
# ================================

# 🔹 Create and Write to a Text File
with open("example.txt", "w") as file:
    file.write("Hello Paul!\n")
    file.write("Hope this works.\n")
    file.write("Yes it works.\n")
    file.write("Great to see it\n")
    file.write("And it worked again.\n")

# 🔹 Read the File
with open("example.txt", "r") as file:
    content = file.read()
    print("📖 File Contents:")
    print(content)

# 🔹 Append New Content
with open("example.txt", "a") as file:
    file.write("Adding a new line to the file.\n")

# 🔹 Read Again After Appending
with open("example.txt", "r") as file:
    updated_content = file.read()
    print("📖 Updated File Contents:")
    print(updated_content)

# 🔹 Read File Line by Line
print("📄 Reading line by line:")
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())

# 🔹 Using try/except to safely open a file
try:
    with open("non_existent.txt", "r") as file:
        data = file.read()
except FileNotFoundError:
    print("⚠️ File not found!")
#!===================================