class LinearCongruentialGenerator:
    def __init__(self, seed, a, c, m):
        self.state = seed
        self.a = a
        self.c = c
        self.m = m

    def next_random(self):
        self.state = (self.a * self.state + self.c) % self.m
        return self.state

lcg = LinearCongruentialGenerator(seed=42, a=1664525, c=1013904223, m=2**32)
for _ in range(10):
    print(lcg.next_random())
