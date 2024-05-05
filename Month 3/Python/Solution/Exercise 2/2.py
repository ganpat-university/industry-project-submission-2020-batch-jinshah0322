num = [i for i in range(1, 20)]
even = filter(lambda x: x % 2 == 0,num)
print(list(even))