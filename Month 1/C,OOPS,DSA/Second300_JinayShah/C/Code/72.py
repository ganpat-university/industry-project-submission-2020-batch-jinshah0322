# file 72.py
# A basic example using NumPy's FFT implementation
import numpy as np

def fft_example(data):
    return np.fft.fft(data)

# Example usage:
data = [1, 2, 3, 4]
fft_result = fft_example(data)
print("FFT Result:", fft_result)
