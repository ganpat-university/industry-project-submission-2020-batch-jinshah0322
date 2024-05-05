lst1 = ['a','b','c','d','e']
lst2 = [1,2,3,4,5]
dictionary = {}
for i in range(len(lst1)):
    dictionary[lst1[i]] = lst2[i]

print(dictionary)