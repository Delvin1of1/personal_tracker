
students = {}

def add_student():
    name = input("Enter the student's name: ")
    age = int(input("Enter the student's age: "))
    grade = int(input("Enter the student's grade: "))
    
    # Add the student to the dictionary
    students[name] = {'age': age, 'grade': grade}
    print(f"Student {name} added successfully!")

# Step 3: Define a function to update an existing student's record
def update_student():
    name = input("Enter the name of the student you want to update: ")
    
    if name in students:
        print(f"Current record for {name}: {students[name]}")
        age = int(input("Enter the new age (or press Enter to keep current): "))
        grade = int(input("Enter the new grade (or press Enter to keep current): "))
        
        # Update the student's record
        students[name] = {'age': age, 'grade': grade}
        print(f"Student {name} updated successfully!")
    else:
        print(f"Student {name} not found.")

# calculate and display the average grade of all students
def calculate_average_grade():
    if not students:
        print("No students in the record.")
        return
    
    total_grades = sum(student['grade'] for student in students.values())
    average_grade = total_grades / len(students)
    print(f"The average grade of all students is: {average_grade}")

# Step 5: Define a function to display all student records
def display_students():
    if not students:
        print("No students in the record.")
        return
    
    print("\nStudent Records:")
    for name, info in students.items():
        print(f"Name: {name}, Age: {info['age']}, Grade: {info['grade']}")

# Step 6: Define the main function to manage the program
def main():
    while True:
        print("\nStudent Record Management System")
        print("1. Add a new student")
        print("2. Update an existing student")
        print("3. Calculate the average grade")
        print("4. Display all student records")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            update_student()
        elif choice == '3':
            calculate_average_grade()
        elif choice == '4':
            display_students()
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# calling Main
if __name__ == "__main__":
    main()