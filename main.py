# This program contains different Python concepts like:
# 1. Class and Object
# 2. Functions
# 3. For Loop
# 4. List
# 5. List Comprehension

# -----------------------------
# Class and Object
# -----------------------------

# Creating a Student class
class Student:

    # This constructor stores the student's information
    def __init__(self, name, age, faculty, marks):
        self.name = name
        self.age = age
        self.faculty = faculty
        self.marks = marks

    # This function prints the student's details
    def display(self):
        print("\nStudent Details")
        print("----------------")
        print("Name    :", self.name)
        print("Age     :", self.age)
        print("Faculty :", self.faculty)
        print("Marks   :", self.marks)

    # This function calculates the average marks
    def average_marks(self):
        return sum(self.marks) / len(self.marks)


# Creating an object of Student class
student1 = Student(
    "Dipak",
    21,
    "Computer Engineering",
    [80, 85, 90, 88]
)

# Calling the display function
student1.display()

# Printing average marks
print("Average Marks:", student1.average_marks())


# -----------------------------
# Functions
# -----------------------------

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
    # Checking if the second number is zero
    if b == 0:
        return "Cannot divide by zero."
    return a / b


# Taking two numbers
num1 = 10
num2 = 5

print("\nCalculator Result")
print("------------------")
print("Addition       :", add(num1, num2))
print("Subtraction    :", subtract(num1, num2))
print("Multiplication :", multiply(num1, num2))
print("Division       :", divide(num1, num2))


# -----------------------------
# List
# -----------------------------

# List of student names
students = ["Dipak", "Hari", "Ram", "Sita", "Gita"]

print("\nStudent Names")
print("-------------")

# Printing each student's name
for student in students:
    print(student)


# -----------------------------
# For Loop
# -----------------------------

print("\nNumbers from 1 to 10")
print("--------------------")

# Printing numbers from 1 to 10
for i in range(1, 11):
    print(i)


# Printing even numbers
print("\nEven Numbers")
print("------------")

for i in range(2, 21, 2):
    print(i)


# -----------------------------
# List Comprehension
# -----------------------------

# Original list
numbers = [1, 2, 3, 4, 5]

# Creating another list with square values
squared = [num ** 2 for num in numbers]

print("\nOriginal Numbers :", numbers)
print("Squared Numbers :", squared)


# Creating a list of even numbers
even_numbers = [num for num in numbers if num % 2 == 0]

print("Even Numbers :", even_numbers)


# Finding the total of all numbers
total = sum(numbers)

print("Total of Numbers :", total)


# End of the program
print("\nProgram executed successfully.")
