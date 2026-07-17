class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

a=int(input("enter the value"))
for a in range (1,10):
    print(a)
student1 = Student("Dipak", 21)
student1.display()


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


print(add(10, 5))
print(subtract(10, 5))
print(multiply(10, 5))
print(divide(10, 5))


students = ["Dipak", "Hari", "Ram", "Sita"]

for student in students:
    print(student)


for i in range(1, 11):
    print(i)


numbers = [1, 2, 3, 4, 5]

squared = [num ** 2 for num in numbers]

print(squared)
