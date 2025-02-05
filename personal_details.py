# Create a program that will:
# Store personal details (like name, age, and favorite colors) in variables and dictionaries.
# Store a list of friends' names.
# Allow a user to update their personal information, like age and favorite color.
# Remove a friend from the list.
# Display the updated information in an organized format.


# Function to display personal information
# def display_info(name, age, favorite_colors, friends):
#     print("\nPersonal Information")
#     print(f"Name: {name}")
#     print(f"Age: {age}")
#     print(f"Favorite Colors: {(favorite_colors)}")
#     print(f"Friends: {(friends)}")

# #personal details
# personal_info = {
#     "name": "Anthony Davis",
#     "age": 25,
#     "favorite_colors": ["Purple", "Gold"]
# }

# #list of friends
# friends_list = ["Lebron", "Vando", "Reeves"]

# # Display initial information
# display_info(personal_info["name"], personal_info["age"], personal_info["favorite_colors"], friends_list)

# # Allow user to update their information
# def update_info():
#     print("Update your personal information:")
#     new_age = input("Enter your new age: ")
#     new_color = input("Enter a new favorite color: ")

#     # Update age and favorite colors
#     personal_info["age"] = int(new_age)
#     personal_info["favorite_colors"].append(new_color)

#     print("\nInformation updated successfully!")
#     display_info(personal_info["name"], personal_info["age"], personal_info["favorite_colors"], friends_list)

# # Allow user to remove a friend
# def remove_friend():
#     print("Current friends list:", (friends_list))
#     friend_to_remove = input("Enter the name of the friend you want to remove: ")

#     if friend_to_remove in friends_list:
#         friends_list.remove(friend_to_remove)
#         print(f"\n{friend_to_remove} has been removed from your friends list.")
#     else:
#         print(f"\n{friend_to_remove} is not in your friends list.")

#     display_info(personal_info["name"], personal_info["age"], personal_info["favorite_colors"], friends_list)

# # Main menu
# while True:
#     print("\nMenu")
#     print("1. Update personal information")
#     print("2. Remove a friend")
#     print("3. Display current information")
#     print("4. Exit")
#     choice = input("Enter your choice (1-4): ")

#     if choice == "1":
#         update_info()
#     elif choice == "2":
#         remove_friend()
#     elif choice == "3":
#         display_info(personal_info["name"], personal_info["age"], personal_info["favorite_colors"], friends_list)
#     elif choice == "4":
#         print("Exiting the program. Goodbye!")
#         break
#     else:
#         print("Invalid choice. Please try again.")

# Simple Personal Info Manager

# Function to get user input and store personal details
def get_user_info():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    favorite_colors = input("Enter your favorite colors (comma-separated): ").split(",")
    friends = input("Enter friends' names (comma-separated): ").split(",")
    return {"name": name, "age": age, "favorite_colors": favorite_colors, "friends": friends}

# Function to update the user's age
def update_age(user_info):
    user_info["age"] = int(input("Enter new age: "))

# Function to update the user's favorite colors
def update_colors(user_info):
    user_info["favorite_colors"] = input("Enter new favorite colors (comma-separated): ").split(",")

# Function to remove a friend from the list
def remove_friend(user_info):
    friend = input("Enter friend's name to remove: ")
    if friend in user_info["friends"]:
        user_info["friends"].remove(friend)
        print(f"{friend} removed!")
    else:
        print("Friend not found!")

# Function to display updated user information
def display_info(user_info):
    print("\nUpdated Information:")
    print(f"Name: {user_info['name']}")
    print(f"Age: {user_info['age']}")
    print(f"Favorite Colors: {', '.join(user_info['favorite_colors'])}")
    print(f"Friends: {', '.join(user_info['friends'])}")

# Main function to handle user choices
def main():
    user_info = get_user_info()  # Collect initial user data
    options = {"1": update_age, "2": update_colors, "3": remove_friend, "4": display_info}
    
    while True:
        # Display menu options
        choice = input("\n1. Update Age\n2. Update Favorite Colors\n3. Remove a Friend\n4. Display Info\n5. Exit\nChoose an option: ")
        if choice == "5":
            break  # Exit the loop
        elif choice in options:
            options[choice](user_info)  # Call the corresponding function
        else:
            print("Invalid choice!")

# Run the program if executed directly
if __name__ == "__main__":
    main()
