class DSU:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.size = [1] * (n+1)
        self.undo_steps = dict()  # Maps day to list of undo steps

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y, day):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return
        # Ensure x_root is the larger tree