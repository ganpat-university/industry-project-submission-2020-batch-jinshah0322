class WaveletMatrix:
    def __init__(self, sequence):
        self.alphabet_size = max(sequence) + 1
        self.matrix = [None] * self.alphabet_size
        self.bitmaps = []

        for level in range(self.alphabet_size.bit_length() - 1, -1, -1):
            bitmaps = [0] * len(sequence)
            low = 0
            high = len(sequence)

            for i, symbol in enumerate(sequence):
                if (symbol >> level) & 1:
                    bitmaps[i] = 1
                    self.matrix[symbol] = self.matrix[symbol] or [0] * high
                    self.matrix[symbol][i] = 1
                    high -= 1
                else:
                    low += 1

            self.bitmaps.append(bitmaps)

    def rank(self, symbol, position):
        result = 0

        for level, bitmap in enumerate(self.bitmaps):
            result += bitmap[position] * ((symbol >> level) & 1)
            position = result + bitmap[position]

        return result

    def select(self, symbol, k):
        low = 0
        high = len(self.bitmaps[0])

        for level, bitmap in enumerate(self.bitmaps):
            low = bitmap[low:high].index((symbol >> level) & 1) + self.rank(symbol, low)
            high = bitmap[low:high].count((symbol >> level) & 1) + low

        return low


sequence = [1, 0, 2, 1, 2, 1, 0, 2, 0, 1]
wavelet_matrix = WaveletMatrix(sequence)


print("Rank of 1 at position 7:", wavelet_matrix.rank(1, 7))  


print("Position of the 3rd occurrence of 2:", wavelet_matrix.select(2, 3))  
