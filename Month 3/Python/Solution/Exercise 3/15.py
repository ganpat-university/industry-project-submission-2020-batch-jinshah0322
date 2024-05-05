import pickle
file = open("my_variables.data","wb")
num = 5
str = "hello"
pickle.dump(num,file)
pickle.dump(str,file)
file.close()