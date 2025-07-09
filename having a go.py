# Loop that prints Hello! 5 times
for _ in range(5):
    print("Hello!")

# Your original greet function — still works great
def greet(name, country, city, university, subjects, age, work):
    print(f"Hello, {name}! Are you from {country}? Which city do you live in {city}?")
    print(f"And you study at {university}. What subjects do you study? {subjects}.")
    print(f"How old are you? {age}. Do you do any part-time work? {work}")

# Calling greet function three times
greet("Alice", "Germany", "Berlin", "Berlin University", "Physics, Math", 21, "Yes")
greet("Bill", "Scotland", "Glasgow", "University of Glasgow", "History, English", 19, "No")
greet("Jean", "Holland", "Amsterdam", "Leiden University", "Biology, Chemistry", 22, "Yes")

# Now the corrected students list (dictionaries)
students = [
    {
        "name": "Alice",
        "country": "Germany",
        "city": "Berlin",
        "university": "Berlin University",
        "subjects": "Physics, Math",
        "age": 21,
        "has_work": True,
        "job_type": "tutor"
    },
    {
        "name": "Bill",
        "country": "Scotland",
        "city": "Glasgow",
        "university": "University of Glasgow",
        "subjects": "History, English",
        "age": 19,
        "has_work": False,
        "job_type": ""
    },
    {
        "name": "Jean",
        "country": "Holland",
        "city": "Amsterdam",
        "university": "Leiden University",
        "subjects": "Biology, Chemistry",
        "age": 22,
        "has_work": True,
        "job_type": "lab assistant"
    }
]

# Function to greet each student based on the dictionary
def greet_from_dict(student):
    print(f"Hello, {student['name']}! Are you from {student['country']}?")
    print(f"You live in {student['city']} and study at {student['university']}.")
    print(f"You’re {student['age']} years old and study {student['subjects']}.")
    if student["has_work"]:
        print(f"You also work part-time as a {student['job_type']}.")
    else:
        print("You don't do any part-time work.")
    print("-" * 50)

# Loop through students and greet each one
for s in students:
    greet_from_dict(s)
# ==================================================================================================


class Birds:
    def __init__(self, name, group, habitats, migratory):
        """Initialize a bird with its characteristics"""
        self.name = name
        self.group = group  # e.g. songbird, raptor, waterfowl
        self.habitats = habitats 
        self.migratory = migratory  # True if the bird migrates seasonally

    def bird_info(self):
        """Display the bird's information"""
        print(f"\n🐦 Bird: {self.name}")
        print(f"Group: {self.group}")
        print(f"Habitats: {', '.join(self.habitats)}")
        print(f"Migratory: {'Yes' if self.migratory else 'No'}")

    def call(self):
        """Placeholder for bird call"""
        print(f"{self.name} sings a beautiful song!")

# Example birds
robin = Birds("Robin", "Songbird", ["Woodland", "Urban"], True)
blackbird = Birds("Blackbird", "Songbird", ["Woodland", "Urban"], True)
house_sparrow = Birds("House Sparrow", "Songbird", ["Urban", "Rural"], False)
shelduck = Birds("Shelduck", "Waterfowl", ["Wetlands", "Coastal"], True)
wigeon = Birds("Wigeon", "Waterfowl", ["Wetlands", "Coastal"], True)
goosander = Birds("Goosander", "Waterfowl", ["Wetlands", "Coastal"], True)
sparrowhawk = Birds("Sparrowhawk", "Raptor", ["Woodland", "Urban"], False)
buzzard = Birds("Buzzard", "Raptor", ["Woodland", "Open fields"], True)
kestrel = Birds("Kestrel", "Raptor", ["Open fields", "Urban"], True)
puffin = Birds("Puffin", "Seabird", ["Coastal", "Marine"], True)
herring_gull = Birds("Herring Gull", "Seabird", ["Coastal", "Marine"], False)
guillemot = Birds("Guillemot", "Seabird", ["Coastal", "Marine"], True)
# Display info and call for selected birds
for bird in [robin, buzzard, puffin]:
    bird.bird_info()
    bird.call()
    


# Demo the bird methods
print("\n" + "="*50)
print("BIRD INFORMATION")
print("="*50)

# Show info for a few birds
robin.bird_info()
robin.call()


        
      
       
    