import sys
reader = (line.rstrip() for line in sys.stdin)
input = reader.__next__

class SegmentTree() :
	def __init__(self, size):
		N = 1
		while N < size:
			N <<= 1
			self.N = N
			self.tree = [0] * (2 * N)

	def update(self, index, value) :
		index += self.N
		self.tree[index] = value
		flag = False
		while index > 1 :
			if flag :
				self.tree[index >> 1] = self.tree[index] ^ self.tree[index ^ 1]
			else :
				self.tree[index >> 1] = self.tree[index] | self.tree[index ^ 1]
			flag = not 