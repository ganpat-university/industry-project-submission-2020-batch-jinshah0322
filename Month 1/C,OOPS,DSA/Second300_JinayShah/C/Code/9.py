def is_harshad_number(number):
    digit_sum = sum(int(digit) for digit in str(number))

    return number % digit_sum == 0

input_number = int(input("Enter a number: "))

if is_harshad_number(input_number):
    print(f"{input_number} is a Harshad number.")
else:
    print(f"{input_number} is not a Harshad number.")
