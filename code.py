class FenwickTree:
    def __init__(self, size):
        self.n = size
        self.tree = [0] * (self.n + 1)  # 1-based indexing

    def update(self, idx, delta):
        while idx <= self.n:
            self.tree[idx] = (self.tree[idx] + delta) % 2
            idx += idx & -idx

    def query(self, idx):
        res = 0
        while idx > 0:
            res = (res + self.tree[idx]) % 2
            idx -= idx & -idx
        return res

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,