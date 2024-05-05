def check(str):
    assert len(str)>=10 , "String length must be greater than or equal then 10"

str = "abcdefghijklmnopqrstuvwxyz"
try:
    check(str)
    print("Length of string is valid")
except AssertionError as e:
    print(e)

str1 = "abc"
try:
    check(str1)
    print("Length of string is valid")
except AssertionError as e:
    print(e)