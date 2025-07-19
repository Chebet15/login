import json
import os

# File where we store users
USER_FILE = "users.json"

# Load users from file if it exists
if os.path.exists(USER_FILE):
    with open(USER_FILE, "r") as f:
        users = json.load(f)
else:
    users = {"admin": "1234", "caro": "pass"}  # default users

while True:
    print("\n=== Welcome ===")
    print("1. Login")
    print("2. Register")
    print("3. Exit")

    choice = input("Choose an option (1/2/3): ")

    if choice == "1":
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username in users and users[username] == password:
            print(f"Login successful! Welcome, {username}")
        else:
            print("Login failed! Wrong username or password.")

    elif choice == "2":
        new_username = input("Choose a username: ")
        if new_username in users:
            print("Username already exists. Try again.")
        else:
            new_password = input("Choose a password: ")
            users[new_username] = new_password

            # Save users to file
            with open(USER_FILE, "w") as f:
                json.dump(users, f)

            print(f"User '{new_username}' registered successfully!")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose 1, 2, or 3.")
