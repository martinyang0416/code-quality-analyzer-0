class Edge:
    def __init__(self, to, rev, capacity):
        self.to = to
        self.rev = rev
        self.capacity = capacity

def putaway(A, B, T, X, Y, W, S):
    # Check each toy can be handled
    for i in range(T):
        can_weak = any(W[i] < x for x in X)
        can_small = any(S[i] < y for y in Y)
        if not (can_weak or can_small):
            return -1

    # Binary search parameters
    low, high, ans = 1, T, -1
    while low <= high:
        mid = (low + high) // 2
      