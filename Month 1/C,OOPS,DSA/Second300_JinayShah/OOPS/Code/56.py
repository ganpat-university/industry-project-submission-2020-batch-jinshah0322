from fractions import Fraction
import numpy as np

class ShorsAlgorithm:
    def __init__(self, N):
        self.N = N
        self.a = 2  

    def quantum_phase_estimation(self):
        measured_phase = 0.5  
        r_guess = self.find_period(measured_phase)
        return r_guess

    def find_period(self, measured_phase):
        frac = Fraction(measured_phase).limit_denominator(self.N)
        return frac.denominator

    def shors_algorithm(self):
        r_guess = self.quantum_phase_estimation()
        x = self.a**(r_guess // 2) % self.N
        factors = np.gcd(x - 1, self.N), np.gcd(x + 1, self.N)
        return factors
if __name__ == "__main__":
    N = 15
    shor = ShorsAlgorithm(N)
    factors = shor.shors_algorithm()
    print(f"Factors of {N}: {factors}")