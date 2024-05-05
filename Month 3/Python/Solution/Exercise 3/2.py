# try:
#     if True
#         print("Hello")
# except SyntaxError as e:
#     print("SyntaxError:", e)

# try:
#      print("Hello")
# except IndentationError as e:
#     print("IndentationError:", e)

# try:
#     print(my_variable)
# except NameError as e:
#     print("NameError:", e)

# try:
#     result = 10 + "5"
# except TypeError as e:
#     print("TypeError:", e)

try:
    number = int("abc")
except ValueError as e:
    print("ValueError:", e)
