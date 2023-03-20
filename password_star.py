MIN_PASSWORD_LENGTH = 8
password = ""

while len(password) < MIN_PASSWORD_LENGTH:
    password = input("Please enter a password: ")
    if len(password) < MIN_PASSWORD_LENGTH:
        print(f"Error: Password must be at least {MIN_PASSWORD_LENGTH} characters long.")

print("*" * len(password))
