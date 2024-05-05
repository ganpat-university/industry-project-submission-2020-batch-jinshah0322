lstTuple = [(1, 2), (3, 4), (5, 6)]
dictionary = dict()
for i in range(0,len(lstTuple)):
    dictionary[i+1] = lstTuple[i]
print(dictionary)