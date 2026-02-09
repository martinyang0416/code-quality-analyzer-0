def putaway(A, B, T, X, Y, W, S):
    # Compute max_X and max_Y
    if A == 0:
        max_X = 0
    else:
        max_X = max(X)
    if B == 0:
        max_Y = 0
    else:
        max_Y = max(Y)
    
    mandatory_w = 0
    mandatory_s = 0
    flexible = 0

    for i in range(T):
        w = W[i]
        s = S[i]
        is_weak = (A > 0 and w < max_X)
        is_small = (B > 0 and s < max_Y)
        
        if not (is_weak or is_small):
            return -1
        if is_weak and not is_smal