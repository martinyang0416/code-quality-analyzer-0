import bisect

def putaway(A, B, T, X, Y, W, S):
    X_sorted = sorted(X)
    Y_sorted = sorted(Y)
    
    can_weak_list = [False] * T
    can_small_list = [False] * T
    
    for i in range(T):
        w = W[i]
        s = S[i]
        # Check can_weak
        idx = bisect.bisect_right(X_sorted, w)
        can_weak = (idx < len(X_sorted))
        can_weak_list[i] = can_weak
        # Check can_small
        idx2 = bisect.bisect_right(Y_sorted, s)
        can_small = (idx2 < len(Y_sorted))
   