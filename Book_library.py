# Project Assignment: Book Title Library
# Objective:
# Create a simple Book Title Library program that allows users to manage a list of book titles.


# Requirements:
# Store book titles using a list.
# Provide a menu where users can choose different actions.
# Allow users to:
# Add a new book to the list.
# Remove a book from the list.
# View all books in the library.
# Exit the program.
# Validate user input to ensure the program does not crash if incorrect input is given.
# Use only:
# Variables
# Lists
# Loops (while and for)
# Conditionals (if-else)
# input() and print()


#OUTPUT
# Welcome to the Book Title Library!


# Choose an option:
# 1. Add a Book
# 2. Remove a Book
# 3. View All Books
# 4. Exit


# Enter your choice: 1
# Enter the book title: Harry Potter
# "Harry Potter" has been added to the library.


# Enter your choice: 3
# Books in the Library:
# - Harry Potter


# Enter your choice: 2
# Enter the book title to remove: Harry Potter
# "Harry Potter" has been removed from the library.


# Enter your choice: 4
# Goodbye!


#Welcome message
Greeting = "welcome to the book library!"
all_caps = Greeting.upper()
print(all_caps)


Book_library = []


while True:
    print(f"\n-----Menu-----")
    print(f"1. Add a book")
    print(f"2. Remove a book")
    print(f"3. View all books")
    print(f"4. Eixt")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_a_book = input("Enter the book Title: ").title()
        Book_library.append(add_a_book)
        print(f"{add_a_book} has been added successfully!",)
    elif choice == "2":
        remove_a_book = input("Enter the book title to remove: ").title()
        if remove_a_book in Book_library:
             Book_library.remove(remove_a_book)
             print(f"You have successfully removed {remove_a_book}")
    elif choice == "3":
        print(Book_library)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid input, try again!")
    



    

   



