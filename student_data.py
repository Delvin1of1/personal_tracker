# Student Management System with Student Details

# Objective:
# Create a Student Management System that allows users to manage a list of students, their courses, and additional details such as age and grade.

# Requirements:
# * Store student details (name, age, grade, and course) using a dictionary.
# * Provide a menu where users can choose different actions.
#   Allow users to:
#     * Add a new student with their name, age, grade, and course.
#     * Remove a student from the system.
#     * View one Student.
#     * View all students and their details (name, age, grade, and course).
#     * Exit the program.
# * Validate user input to ensure the program does not crash if incorrect input is given.

# Use only:
# Variables
# Lists & Dictionaries
# Loops (while and for)
# Conditionals (if-else)
# input() and print()

# Example Flow
# Welcome to the Student Management System!

# Choose an option:
# 1. Add a Student, collect (name, age, grade and a list of courses)
# 2. Remove a Student
# 3. View one Student
# 3. View All Students
# 4. Exit

# Enter your choice: 1
#  * Enter student name: John
#  * Enter student age: 20
#  * Enter student grade: A
#  * Enter student course: Computer Science
#  Print {student_name} has been added to the system.

# Enter your choice: 3
# Students in the system:
# - John, Age: 20, Grade: A, Course: Computer Science

# Enter your choice: 2
# Enter student name to remove: John
# John has been removed from the system.

# Enter your choice: 4
# Goodbye!

# Submission Link: Assigment Submission

greeting = "Welcome to the student management system!"
print(greeting.title())

student_manger = {}

while True:
    print("\nStudent Manger")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. View All Students")
    print("4. View One Student")
    print("5. Exit")
    
    choice = input("Enter your choice (1 - 5): ")

    if choice == "1":

        name = input("Enter student's name: ").lower()
        age = input("Enter student's age: ")
        grade = input("Enter student's grade: ")
        course = input("Enter student's course: ")

        student_manger[name] = {
            "age": age,
            "grade": grade,
            "course": course,
        }
        print(f"{name} has been added successfully!")

    elif choice == "2":
        remove_student = input("Enter student's name to remove: ")
        if remove_student in student_manger:
            student_manger.pop(remove_student)
            print(f"{remove_student} has been removed successfully!")
        else:
            print("Name not found")

    elif choice == "3":
        print("Student Data: ")
        for name, details in student_manger.items():
            # print(student_manger.items())
            print(f"Name: {name}, Age: {details["age"]}, Grade: {details["grade"]}, Course: {details["course"]}")

    elif choice == "4":
        view_student = input("Enter the name of the student you want to view: ")
        if view_student in student_manger:
            details = student_manger[view_student]  # Accessing the value using the key
            print(f"Name: {view_student}, Age: {details["age"]}, Grade: {details["grade"]}, Course: {details["course"]}")
        else:
            print(f"{view_student} not found in the records.")


    elif choice == "5":
        print("Goodbye!")
    
    else:
        print("Invalid Input!")


# name = input("Enter student name: ")
# age = int(input("Enter student's age: "))
# grade = input("Enter student's grade: ")
# courses = input("Enter student's course: ")
# student_details = {"name": name,
#                    "age": age,
#                    "grade": grade,
#                    "courses": courses,

# }
# student_manger.update(student_details)
# print(student_manger)
# # # remove()
# # remove_student = input("Enter name of student to remove: ")
# # if remove_student in student_details:
    

