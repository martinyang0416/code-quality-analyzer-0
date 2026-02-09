import bisect

def putaway(A, B, T, X, Y, W, S):
    sorted_X = sorted(X)
    sorted_Y = sorted(Y)
    
    W_only = 0
    S_only = 0
    Both = 0
    
    for i in range(T):
        w = W[i]
        s = S[i]
        # Check if can be handled by weak robots
        idx_x = bisect.bisect_right(sorted_X, w)
        weak_ok = idx_x < len(sorted_X)
        
        # Check if can be handled by small robots
        idx_y = bisect.bisect_right(sorted_Y, s)
        small_ok = idx_y < len(sorted_Y)
    