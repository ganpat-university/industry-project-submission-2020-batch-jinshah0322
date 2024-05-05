import random

def reservoir_sampling(stream, k):    
    reservoir = [stream[i] for i in range(k)]
    for i in range(k, len(stream)):
        j = random.randint(0, i)        
        if j < k:
            reservoir[j] = stream[i]

    return reservoir


stream = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 3
result = reservoir_sampling(stream, k)
print("Random sample:", result)
