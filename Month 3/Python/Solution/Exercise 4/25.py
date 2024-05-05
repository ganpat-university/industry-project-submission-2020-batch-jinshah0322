import string
import random
lst = [random.choice(string.ascii_letters) for _ in range(10)]
print(''.join(lst))