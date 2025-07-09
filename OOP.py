# Student class
class Student:
    def __init__(self, name, age, email, college, studying, course, address, hobbies=None):
        self.name = name
        self.age = age
        self.email = email
        self.college = college
        self.studying = studying
        self.course = course
        self.address = address
        self.hobbies = hobbies if hobbies else []

    def introduce(self):
        print(f"Hi, my name is {self.name}. I am {self.age} years old, studying {self.studying} "
              f"({self.course}) at {self.college}. You can contact me at {self.email}. I live at {self.address}.")
        if self.hobbies:
            print(f"My hobbies are: {', '.join(self.hobbies)}")

    def update_email(self, new_email):
        self.email = new_email
        print(f"{self.name}'s email has been updated to {self.email}")

# Create student objects
student1 = Student(
    "Emily", 21, "emily@example.com", "Lancaster College",
    "Computer Science", "Python Development", "12 Fisherman's Lane, Lancaster",
    hobbies=["fishing", "reading"]
)

student2 = Student(
    "John", 22, "john@example.com", "Lancaster College",
    "Mathematics", "Statistics", "34 River Road, Lancaster",
    hobbies=["cycling"]
)

student3 = Student(
    "Alice", 20, "alice@example.com", "Lancaster College",
    "Physics", "Quantum Mechanics", "56 Hill Street, Lancaster"
)

# Call introduce method
student1.introduce()
student2.introduce()
student3.introduce()

# Update email example
student1.update_email("emily.new@example.com")


#