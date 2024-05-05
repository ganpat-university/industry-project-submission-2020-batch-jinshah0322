def add_numbers(num1, num2):
    if not (isinstance(num1, (int, float)) and isinstance(num2, (int, float))):
        raise TypeError("Both numbers must be either float or integer")
    return num1 + num2

try:
    result = add_numbers(5, 3.5)
    print("Result:", result)
except TypeError as e:
    print("Error:", e)
