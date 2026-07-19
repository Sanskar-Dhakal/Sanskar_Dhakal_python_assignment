passwords = ["hello", "Hello123", "H3ll0@World", "12345678", "MyP@ss!"]

special_chars = "!@#$%^&*"

for password in passwords:
    print("\nChecking Password:", password)

    missing = []

    # Check length
    if len(password) < 8:
        missing.append("At least 8 characters")

    # Check uppercase
    if not any(char.isupper() for char in password):
        missing.append("At least one uppercase letter")

    # Check lowercase
    if not any(char.islower() for char in password):
        missing.append("At least one lowercase letter")

    # Check digit
    if not any(char.isdigit() for char in password):
        missing.append("At least one digit")

    # Check special character
    if not any(char in special_chars for char in password):
        missing.append("At least one special character (!@#$%^&*)")

    # Display result
    if len(missing) == 0:
        print("Strong Password")
    else:
        print("Weak Password")
        print("Missing Criteria:")
        for item in missing:
            print("-", item)