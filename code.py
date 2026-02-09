MOD = 10**9 + 7

def main():
    import sys
    input = sys.stdin.read().split()
    m = int(input[0])
    b = list(map(int, input[1:m+1]))
    
    # Assign ranks in decreasing order
    sorted_b = sorted(b, reverse=True)
    rank = {v:i+1 for i, v in enumerate(sorted_b)}
    r = [rank[v] for v in b]
    
    class FenwickTree:
        def __init__(self, size):
            self.n = size
            self.tree = [0] * (self.n + 2)
        
        def update(self, idx, delta):
            while i