import string
dictionary = {}
str = string.ascii_lowercase + string.ascii_uppercase + "0123456789"
for i in str:
    dictionary[i] = ord(i)
print(dictionary)