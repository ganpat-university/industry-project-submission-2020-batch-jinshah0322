import random

def select_random_from_stream(stream):
    selected_number = None
    count = 0

    for index, number in enumerate(stream):
        count += 1

        
        if random.randint(1, count) == 1:
            selected_number = number

    return selected_number


stream = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random_number = select_random_from_stream(stream)
print(f"Random number from stream: {random_number}")
