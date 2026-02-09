class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.size = 1
        while self.size < self.n:
            self.size <<= 1
        self.tree = [ -float('inf') ] * (2 * self.size)
        for i in range(self.n):
            self.tree[self.size + i] = data[i]
        for i in range(self.size -1, 0, -1):
            self.tree[i] = max(self.tree[2*i], self.tree[2*i +1])
    
    def update(self, pos, value):
        pos += self.size
        self.tree[pos] = value