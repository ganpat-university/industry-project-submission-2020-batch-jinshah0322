import random

def generate():
    generatedNumbers = set()
    while len(generatedNumbers) < 10:
        num = random.randint(1, 100)
        if num not in generatedNumbers:
            generatedNumbers.add(num)
            yield num

random_number_generator = generate()
for number in random_number_generator:
    print(number, end=", ")