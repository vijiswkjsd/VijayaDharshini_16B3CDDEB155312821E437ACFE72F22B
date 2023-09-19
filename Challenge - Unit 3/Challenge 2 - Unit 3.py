class Student:
    def __init__(self, name, roll_number, grade):
        self.name = name
        self.roll_number = roll_number
        self.grade = grade
    def __str__(self):
        return f"Name: {self.name}, Roll Number: {self.roll_number}, grade: {self.grade}"
def compare_by_grade(student):
    return student.grade
def sort_students(student_list):
    student_list.sort(key=compare_by_grade, reverse=True)

students1 = [
    Student("arun", "22CS101", 3.8),
    Student("bharath", "22CS102", 3.5),
    Student("Chiranjeevi", "22CS103", 4.0),
    Student("Deepak", "22CS104", 3.2),
]

students2 = [
    Student("Ezhil", "22CS105", 3.9),
    Student("Faruk", "22CS106", 3.7),
    Student("Gokul", "22CS107", 3.6),
]

sort_students(students1)
sort_students(students2)
print("SORTED BY GRADE")
print("Students list 1:")
for student in students1:
    print(student)

print("Students list 2:")
for student in students2:
    print(student)