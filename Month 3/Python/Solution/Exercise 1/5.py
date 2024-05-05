string_value = input("Enter a string value:")
int_value = int(input("Enter a integer value:"))
float_value = float(input("Enter a float value:"))

if(bool(string_value) == False):
    print(string_value)
else:
    print(bool(string_value))

if(bool(int_value) == False):
    print(int_value)
else:
    print(bool(int_value))

if(bool(float_value) == False):
    print(float_value)
else:
    print(bool(float_value))