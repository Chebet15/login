# Login & Registration System

# Step 1: Store users in a dictionary (username: password)
users = {
    "admin": "1234",
    "caro": "pass"
}

while True:
    print("\n=== Welcome ===")
    print("1. Login")
    print("2. Register")
    print("3. Exit")

    choice = input("Choose an option (1/2/3): ")

    if choice == "1":
        # LOGIN
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username in users and users[username] == password:
            print(f"Login successful! Welcome, {username}")
        else:
            print("Login failed! Wrong username or password.")

    elif choice == "2":
        # REGISTER
        new_username = input("Choose a username: ")
        if new_username in users:
            print("Username already exists. Try again.")
        else:
            new_password = input("Choose a password: ")
            users[new_username] = new_password
            print(f"User '{new_username}' registered successfully!")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("the option is Invalid . Please choose 1, 2, or 3.")
