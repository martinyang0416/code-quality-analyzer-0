class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (4 * self.n)
        self.build(0, self.n - 1, 1, data)
    
    def build(self, l, r, node, data):
        if l == r:
            self.tree[node] = 1 << (ord(data[l]) - ord('a'))
            return
        mid = (l + r) // 2
        self.build(l, mid, 2 * node, data)
        self.build(mid + 1, r, 2 * node + 1, data)
        self.tree[node] = self.tree[2 * node] | self.tree[2 * node + 1]
    
 