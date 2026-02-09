import bisect

def putaway(A, B, T, X, Y, W, S):
    if T == 0:
        return 0

    max_X = -float('inf')
    if A > 0:
        max_X = max(X)
    max_Y = -float('inf')
    if B > 0:
        max_Y = max(Y)

    category1 = []
    category2 = []
    category3 = []

    for i in range(T):
        w = W[i]
        s = S[i]
        eligible_weak = (A > 0) and (w < max_X)
        eligible_small = (B > 0) and (s < max_Y)
        if not eligible_weak and not eligible_small:
            return -1
    