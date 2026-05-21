# ============================================================
# BASIC PYTHON CONCEPTS (Lists, Dictionaries, Loops, Conditionals)
# ============================================================

# ----- LIST EXAMPLE -----
scores = [90, 85, 78]

print("List Example:")
for s in scores:          # Loop through list
    print(" Score:", s)
print()


# ----- DICTIONARY EXAMPLE -----
student = {
    "name": "Alex",
    "grade": 12,
    "GPA": 3.8
}

print("Dictionary Example:")
print(" Name:", student["name"])
print(" GPA:", student["GPA"])
print()


# ----- CONDITIONAL EXAMPLE -----
score = 88
print("Conditional Example:")
if score >= 90:
    print(" Grade: A")
elif score >= 80:
    print(" Grade: B")
else:
    print(" Grade: C or lower")
print()


# ----- LOOP + CONDITION -----
numbers = [3, 8, 12, 5, 20]

print("Loop + Condition Example:")
for n in numbers:
    if n > 10:
        print(n, "is greater than 10")
print()


# ============================================================
# OBJECT-ORIENTED PROGRAMMING (OOP) EXAMPLES
# ============================================================

# This class demonstrates:
# - Constructor (__init__)
# - Attributes
# - Getter method
# - Method with parameter
# - Method without parameter
# - Method returning a value
# - __str__, __eq__, __gt__ overrides

class Student:
    def __init__(self, name, grade):
        # Constructor: runs when object is created
        self.name = name
        self.grade = grade

    # Getter method
    def get_grade(self):
        return self.grade

    # Method with NO parameters
    def say_hello(self):
        print("Hello, I am", self.name)

    # Method WITH a parameter
    def update_grade(self, new_grade):
        self.grade = new_grade

    # Method that RETURNS a value
    def is_passing(self):
        return self.grade >= 70

    # __str__ override (controls print())
    def __str__(self):
        return f"Student(name={self.name}, grade={self.grade})"

    # __eq__ override (== operator)
    def __eq__(self, other):
        return self.grade == other.grade

    # __gt__ override (> operator)
    def __gt__(self, other):
        return self.grade > other.grade


# ============================================================
# USING THE CLASS
# ============================================================

print("OOP Example:")

s1 = Student("Alex", 88)
s2 = Student("Mia", 92)

print(" Printing object:", s1)       # Uses __str__
s1.say_hello()                       # Method with no parameters
print(" Grade:", s1.get_grade())     # Getter method

s1.update_grade(95)                  # Method with parameter
print(" Updated Grade:", s1.get_grade())

print(" Passing?", s1.is_passing())  # Method returning value

print(" Compare == :", s1 == s2)     # Uses __eq__
print(" Compare >  :", s1 > s2)      # Uses __gt__
print()


# ============================================================
# END OF CONSOLIDATED STUDY FILE
# ============================================================
print("All examples completed.")
