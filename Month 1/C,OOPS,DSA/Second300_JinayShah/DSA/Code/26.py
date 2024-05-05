import numpy as np

def random_from_arbitrary_distribution(size, pdf, x_values):
    cdf = np.cumsum(pdf) / np.sum(pdf)  

    uniform_random_numbers = np.random.rand(size)
    random_numbers = np.interp(uniform_random_numbers, cdf, x_values)
    return random_numbers

pdf = np.array([0.2, 0.5, 0.3])  
x_values = np.array([1, 2, 3])  
generated_numbers = random_from_arbitrary_distribution(1000, pdf, x_values)
print(generated_numbers)

