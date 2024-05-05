class BloomFilter:
    def __init__(self, size, hash_count):
        self.size = size
        self.bit_array = [0]*size
        self.hash_count = hash_count

    def add(self, string):
        for seed in range(self.hash_count):
            result = hash(string + str(seed)) % self.size
            self.bit_array[result] = 1

    def lookup(self, string):
        for seed in range(self.hash_count):
            result = hash(string + str(seed)) % self.size
            if self.bit_array[result] == 0:
                return "Not present"
        return "Present"

bf = BloomFilter(50000, 3)
bf.add("dog")
bf.add("fish")
bf.add("cat")

print("Dog is:",bf.lookup("dog"))
print("Bird is:",bf.lookup("bird"))
print("Cat is:",bf.lookup("cat"))
