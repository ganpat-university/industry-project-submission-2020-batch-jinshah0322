import pickle
file = open("my_variables.data","rb")
num = pickle.load(file)
str = pickle.load(file)
print(num,str)
file.close()