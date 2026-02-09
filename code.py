def putaway(A, B, T, X, Y, W, S):
    # Compute max_x and max_y
    if A > 0:
        max_x = max(X)
    else:
        max_x = -1  # since W[i] >=1, so W < -1 is impossible, weak_ok is false
    
    if B > 0:
        max_y = max(Y)
    else:
        max_y = -1
    
    must_weak = 0
    must_small = 0
    opt = 0
    
    for i in range(T):
        w = W[i]
        s = S[i]
        wk_ok = (w < max_x)
        sm_ok = (s < max_y)
        
        if not wk_ok and not sm_ok:
            return -1