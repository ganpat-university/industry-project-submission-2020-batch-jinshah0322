try:
    result = 10 / 2
except ZeroDivisionError as e:
    print("Error:", e)
else:
    print("The result is:", result)
finally:
    print("Completion of the program")