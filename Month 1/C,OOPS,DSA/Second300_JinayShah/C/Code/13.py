def is_buzz_number(number):
    return number % 7 == 0 or number % 10 == 7

input_number = int(input("Enter a number: "))

if is_buzz_number(input_number):
    print(f"{input_number} is a buzz number.")
else:
    print(f"{input_number} is not a buzz number.")