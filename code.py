def putaway(A, B, T, X, Y, W, S):
    if A + B == 0:
        return -1  # impossible as per problem constraints
    
    max_X = -1
    if A > 0:
        max_X = max(X)
    max_Y = -1
    if B > 0:
        max_Y = max(Y)
    
    only_weak = 0
    only_small = 0
    both = 0
    for i in range(T):
        w = W[i]
        s = S[i]
        flag_t1 = (w < max_X) if (A > 0) else False
        flag_t2 = (s < max_Y) if (B > 0) else False
        
        if flag_t1 and flag_t2:
            both += 1
