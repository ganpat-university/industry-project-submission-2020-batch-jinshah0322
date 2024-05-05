import random
lst = [random.randint(0,1) for _ in range(10)]
if all(lst):
    print("ALL")
elif any(lst):
    print("ANY")
else:
    print("NONE")