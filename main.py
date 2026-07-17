# ==========================================================
# Python Basics Program
# Topics Covered:
# 1. Classes and Objects
# 2. Functions
# 3. Loops
# 4. Lists
# 5. List Comprehension
# 6. Exception Handling
# ==========================================================


# ==========================================================
# CLASS AND OBJECT
# ==========================================================

# Create a class named Student
class Student:

    # Constructor
    # This method runs automatically whenever a new object is created.
    def __init__(self, name, age, faculty, marks):
        self.name = name
        self.age = age
        self.faculty = faculty
        self.marks = marks

    # Method to display student details
    def display(self):
        print("\n========== STUDENT INFORMATION ==========")
        print(f"Name    : {self.name}")
        print(f"Age     : {self.age}")
        print(f"Faculty : {self.faculty}")
        print(f"Marks   : {self.marks}")

    # Method to calculate average marks
    def average_marks(self):
        return sum(self.marks) / len(self.marks)


# Create an object of Student class
student1 = Student(
    "Dipak",
    21,
    "Computer Engineering",
    [80, 85, 90, 88]
)

# Call display method
student1.display()

# Print average marks
print(f"Average Marks: {student1.average_marks():.2f}")


# ==========================================================
# FUNCTIONS
# ==========================================================

# Function to add two numbers
def add(a, b):
    return a + b


# Function to subtract two numbers
def subtract(a, b):
    return a - b


# Function to multiply two numbers
def multiply(a, b):
    return a * b


# Function to divide two numbers
def divide(a, b):
    # Prevent division by zero
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b


# Store numbers in variables
num1 = 10
num2 = 5

print("\n========== CALCULATOR ==========")
print(f"{num1} + {num2} = {add(num1, num2)}")
print(f"{num1} - {num2} = {subtract(num1, num2)}")
print(f"{num1} * {num2} = {multiply(num1, num2)}")
print(f"{num1} / {num2} = {divide(num1, num2)}")


# ==========================================================
# LIST
# ==========================================================

# Create a list of students
students = [
    "Dipak",
    "Hari",
    "Ram",
    "Sita",
    "Gita"
]

print("\n========== STUDENT LIST ==========")

# Loop through each student
for student in students:
    print(student)


# ==========================================================
# FOR LOOP
# ==========================================================

print("\n========== NUMBERS FROM 1 TO 10 ==========")

# Print numbers from 1 to 10
for i in range(1, 11):
    print(i)


# ==========================================================
# EVEN NUMBERS
# ==========================================================

print("\n========== EVEN NUMBERS ==========")

# Print even numbers between 1 and 20
for i in range(2, 21, 2):
    print(i)


# ==========================================================
# LIST COMPREHENSION
# ==========================================================

# Original list
numbers = [1, 2, 3, 4, 5]

# Create a new list containing squares
squared = [num ** 2 for num in numbers]

print("\n========== LIST COMPREHENSION ==========")
print("Original Numbers :", numbers)
print("Squared Numbers  :", squared)


# ==========================================================
# FILTER EVEN NUMBERS USING LIST COMPREHENSION
# ==========================================================

# Extract only even numbers
even_numbers = [num for num in numbers if num % 2 == 0]

print("\nEven Numbers:", even_numbers)


# ==========================================================
# SUM OF LIST ELEMENTS
# ==========================================================

# Calculate the sum of all numbers
total = sum(numbers)

print("\n========== SUM OF NUMBERS ==========")
print("Numbers :", numbers)
print("Total   :", total)


# ==========================================================
# PROGRAM COMPLETED
# ==========================================================

print("\n=========================================")
print("Python Basics Program Executed Successfully!")
print("=========================================")
