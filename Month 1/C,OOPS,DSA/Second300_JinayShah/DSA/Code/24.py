import random

def random_0_1_generator():
    return random.randint(0, 1)

def random_0_6_generator():
    
    bit1 = random_0_1_generator()
    bit2 = random_0_1_generator()
    bit3 = random_0_1_generator()

    
    decimal_number = bit1 * 4 + bit2 * 2 + bit3

    
    while decimal_number > 6:
        bit1 = random_0_1_generator()
        bit2 = random_0_1_generator()
        bit3 = random_0_1_generator()
        decimal_number = bit1 * 4 + bit2 * 2 + bit3

    return decimal_number


random_number = random_0_6_generator()
print(f"Random number in [0, 6]: {random_number}")
