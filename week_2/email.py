
'''
emails = []

n = int(input("Enter the number of emails: "))

for i in range(n):
    em = input(f"Enter email {i+1}: ")
    emails.append(em)

print("\nEmail Validation Results:")

for email in emails:
    if "@" not in email:
        print(f"{email}Invalid (missing '@')")
    elif email.startswith("@"):
        print(f"{email} ('@' cannot be at the start)")
    elif "." not in email.split("@")[-1]:
        print(f"{email} Invalid (missing domain extension)")
    elif email.endswith("."):
        print(f"{email} Invalid (cannot end with '.')")
    else:
        print(f"{email} Valid")
'''

import re

emails = []
valid = []
invalid = []

n = int(input("Enter the number of emails: "))

for i in range(n):
    email = input(f"Enter email {i+1}: ")
    emails.append(email)

# Regular expression for email validation
pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

for email in emails:
    if re.fullmatch(pattern, email):
        valid.append(email)
    else:
        invalid.append(email)

print("\nValid Emails:")
for email in valid:
    print(email)

print("\nInvalid Emails:")
for email in invalid:
    print(email)