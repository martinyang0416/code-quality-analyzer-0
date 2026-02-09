import sys

def putaway(A, B, T, X, Y, W, S):
    is_weak = [False] * T
    is_small = [False] * T
    for i in range(T):
        can_weak = any(x > W[i] for x in X)
        can_small = any(y > S[i] for y in Y)
        is_weak[i] = can_weak
        is_small[i] = can_small
        if not can_weak and not can_small:
            return -1

    category1 = []
    category2 = []
    category3 = []
    for i in range(T):
        if is_weak[i] and not is_small[i]:
            category2.append(W[i])
   