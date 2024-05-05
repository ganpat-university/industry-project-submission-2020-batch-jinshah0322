import string

def is_valid_palindrome(s):
    cleaned_s = ''.join(char.lower() for char in s if char.isalnum())

    return cleaned_s == cleaned_s[::-1]

input_string = input("Enter a string: ")
if is_valid_palindrome(input_string):
    print("The string is a valid palindrome.")
else:
    print("The string is not a valid palindrome.")
