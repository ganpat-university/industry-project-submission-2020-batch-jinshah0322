class WaveletTree:

	def __init__(self, from_idx, to_idx, low, high, arr):
	
		self.low = low
		self.high = high
		if from_idx >= to_idx:
			return
		if self.high == self.low:
			self.freq = [0] * (to_idx - from_idx + 2)
			for i in range(from_idx, to_idx + 1):
				self.freq[i - from_idx + 1] = self.freq[i - from_idx] + 1
			return
		mid = (self.low + self.high) // 2
		
		self.freq = [0] * (to_idx - from_idx + 2)
		for i in range(from_idx, to_idx + 1):
			self.freq[i - from_idx + 1] = self.freq[i - from_idx] + (arr[i] <= mid)
		pivot = from_idx
		while pivot <= to_idx and arr[pivot] <= mid:
			pivot += 1
		self.l = WaveletTree(from_idx, pivot - 1, self.low, mid, arr)
		self.r = WaveletTree(pivot, to_idx, mid + 1, self.high, arr)

	def kOrLess(self, l, r, k):
		if l > r or k < self.low:
			return 0
		if self.high <= k:
			return r - l + 1
		LtCount = self.freq[l - 1]
		RtCount = self.freq[r]
		return (
			self.l.kOrLess(LtCount + 1, RtCount, k) +
			self.r.kOrLess(l - LtCount, r - RtCount, k)
		)


size = 5
high = float('-inf')


arr = [1, 2, 3, 4, 5]

for i in range(size):
	high = max(high, arr[i])


obj = WaveletTree(0, size - 1, 1, high, arr)


print(obj.kOrLess(1, 3, 2)) 
