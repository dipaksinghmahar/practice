# ==========================================================
# Python Concepts Demonstration Program
# Author : Dipak
# Description:
# Demonstrates:
# 1. Class and Object
# 2. Functions
# 3. Loops
# 4. Lists
# 5. List Comprehension
# 6. Dictionary
# 7. Exception Handling
# 8. File Handling
# ==========================================================

# -------------------------------
# Class and Object
# -------------------------------

class Student:
    """Represents a student."""

    def __init__(self, name: str, age: int, faculty: str, marks: list[int]):
        self.name = name
        self.age = age
        self.faculty = faculty
        self.marks = marks

    def display(self):
        print("\n========== Student Details ==========")
        print(f"Name     : {self.name}")
        print(f"Age      : {self.age}")
        print(f"Faculty  : {self.faculty}")
        print(f"Marks    : {self.marks}")

    def average_marks(self):
        return sum(self.marks) / len(self.marks)

    def grade(self):
        avg = self.average_marks()

        if avg >= 90:
            return "A+"
        elif avg >= 80:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 60:
            return "C"
        else:
            return "Fail"


student = Student(
    "Dipak",
    21,
    "Computer Engineering",
    [80, 85, 90, 88]
)

student.display()

print(f"Average : {student.average_marks():.2f}")
print(f"Grade   : {student.grade()}")

# -------------------------------
# Functions
# -------------------------------

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero."


num1 = 20
num2 = 5

print("\n========== Calculator ==========")

print("Addition       :", add(num1, num2))
print("Subtraction    :", subtract(num1, num2))
print("Multiplication :", multiply(num1, num2))
print("Division       :", divide(num1, num2))

# -------------------------------
# Lists
# -------------------------------

students = [
    "Dipak",
    "Hari",
    "Ram",
    "Sita",
    "Gita"
]

print("\n========== Student List ==========")

for index, name in enumerate(students, start=1):
    print(f"{index}. {name}")

# -------------------------------
# Loops
# -------------------------------

print("\n========== Numbers 1-10 ==========")

for number in range(1, 11):
    print(number)

print("\n========== Even Numbers ==========")

for number in range(2, 21, 2):
    print(number)

print("\n========== Odd Numbers ==========")

for number in range(1, 20, 2):
    print(number)

# -------------------------------
# List Comprehension
# -------------------------------

numbers = [1, 2, 3, 4, 5]

squares = [num ** 2 for num in numbers]
cubes = [num ** 3 for num in numbers]
even_numbers = [num for num in numbers if num % 2 == 0]

print("\n========== List Comprehension ==========")

print("Numbers :", numbers)
print("Squares :", squares)
print("Cubes   :", cubes)
print("Even    :", even_numbers)

# -------------------------------
# Dictionary
# -------------------------------

student_info = {
    "Name": "Dipak",
    "Age": 21,
    "Faculty": "Computer Engineering"
}

print("\n========== Dictionary ==========")

for key, value in student_info.items():
    print(f"{key}: {value}")

# -------------------------------
# Exception Handling
# -------------------------------

print("\n========== Exception Handling ==========")

try:
    number = int(input("Enter a number: "))
    print("You entered:", number)
except ValueError:
    print("Invalid input! Please enter an integer.")

# -------------------------------
# File Handling
# -------------------------------

print("\n========== File Handling ==========")

try:
    with open("sample.txt", "w") as file:
        file.write("Welcome to Python Programming!\n")
        file.write("This file was created using Python.\n")

    with open("sample.txt", "r") as file:
        print(file.read())

except Exception as error:
    print("Error:", error)

# -------------------------------
# Built-in Functions
# -------------------------------

print("\n========== Built-in Functions ==========")

print("Maximum :", max(numbers))
print("Minimum :", min(numbers))
print("Sum     :", sum(numbers))
print("Length  :", len(numbers))

# -------------------------------
# Lambda Function
# -------------------------------

square = lambda x: x * x

print("\nSquare of 8 :", square(8))

# -------------------------------
# Sorting
# -------------------------------

marks = [80, 65, 90, 55, 76]

print("\n========== Sorting ==========")

print("Original :", marks)
print("Ascending:", sorted(marks))
print("Descending:", sorted(marks, reverse=True))

# -------------------------------
# Program End
# -------------------------------

print("\n===================================")
print("Program executed successfully.")
print("===================================")
