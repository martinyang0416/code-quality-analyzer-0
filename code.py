class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))  # 1-based indexing
        self.rank = [1] * (n + 1)
    
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False  # already in the same set
        if self.rank[pu] > self.rank[pv]:
            self.parent