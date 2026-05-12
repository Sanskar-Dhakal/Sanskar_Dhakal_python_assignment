'''
Question 1:

Write a Python script that:
Asks the user to enter a decimal number (float).
Converts the number into an integer and a string.
Displays all three values (original float, integer, and string) using string formatting.

'''
decimal_number=float(input("Enter a decimal number:"))
integer_number=int(decimal_number)
string_number=str(decimal_number)
print(f"Original float: {decimal_number}")
print(f"Converted to integer: {integer_number}")
print(f"Converted to string: {string_number}",type(string_number))



'''
Question 2:

Write a program that:
Ask the user for their full name.
Extracts the first letter of the first and last name using string slicing.
Displays the initials in uppercase.

'''

Full_name=input("Enter your full name:")
capitalized_name=Full_name.upper()
spliting_name=capitalized_name.split()
output=spliting_name[0][0]+ "," +spliting_name[1][0]
print(f"Your initials are: {output}")


'''
Question 3:

Write a program that:
Takes a string input from the user.
Uses string slicing to reverse it.
Prints the reversed string.
'''

user_input=input("Enter a string ")
slicing_to_reverse=user_input[::-1]
print(f"Reversed string: {slicing_to_reverse}")


'''
Question 4:

Write a program that:
Asks the user to enter a word and a starting index.
Extracts and prints the substring from that index to the end using string slicing.

'''
word=input("Enter a word ")
starting_index=int(input("Enter a starting index "))
substring=word[starting_index:]
print(f"Substring from index : {starting_index} is {substring}")



'''
Question 5:

Write a Python script that:
Asks the user to enter an email address.
Extracts the domain name (part after @) using string slicing.
Prints the extracted domain

'''
email=input("enter your email address ")
slicing_to_extract_domain=email.split("@")
domain=slicing_to_extract_domain[1]
print(f"Domain: {domain}")


'''
Question 6:

Write a Python program that:
Takes a word as input.
Swaps its first and last character using string slicing.
Displays the new word.
'''
word=input("Enter a word: ")
first_char=word[0]
last_char=word[-1]
new_word=last_char + word[1:-1] + first_char
print(f"New_word:{new_word}")

'''
Question 7:

Write a Python program that takes a list of numbers and:
Print the numbers in the list but skip numbers that are divisible by 5.
Stops the loop if a number greater than 50 is encountered.

'''
list_of_numbers=[2,3,4,5,6,7,10,12,15,18,20, 50, 51, 52]
length=len(list_of_numbers)
for i in range(length):
    if list_of_numbers[i]>50:
        break
    elif list_of_numbers[i]%5==0:
        continue
    else:
        print(list_of_numbers[i])

'''
Question 8:

Write a Python program that takes a password as input and checks its strength based on the following conditions:
Weak: If the password is less than 6 characters or only contains letters.
Moderate: If the password has at least 6 characters and contains both letters and numbers.
Strong: If the password has at least 8 characters, contains letters, numbers, and special characters (@, #, $, %, &).

'''
password=input("Enter a password: ")
special="@#$%&"
length=len(password)
if length<6 or password.isalpha():
    print("Weak password")

elif len(password) >= 8 and any(char in special for char in password):
    print("Strong password")

elif length>=6 and password.isalnum():
    print("Moderate password")
else:
    print("Try again")


'''
Question 9:

Write a Python program that takes a string as input and returns a new string where every 
alternate word is reversed while keeping the order of the words intact.

Example Input/Output:
Input: "Python is an amazing programming language"
Output: "Python si an gnizama programming egaugnal" 

'''
string=input("Enter a string: ")
words=string.split()
new_string=""
length=len(words)
for i in range(length):
    if i%2==0:
        new_string+=words[i]+" "
    else:
        new_string+=words[i][::-1]+" "
print(f"New string: {new_string.strip()}")
