file = open("test_file.txt", "r")
data = file.readlines()
for i in data:
    print(i)