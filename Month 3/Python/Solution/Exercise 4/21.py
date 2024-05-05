import random
lst = [random.randint(1,101) for _ in range(1,11)]
even = []
odd = []
for i in lst:
    if i%2==0: even.append(i)
    else: odd.append(i)

print(even,odd)