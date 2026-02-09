def putaway(A, B, T, X, Y, W, S):
    # Compute max_X and max_Y
    max_x = 0
    if A > 0:
        max_x = max(X)
    else:
        max_x = 0
    max_y = 0
    if B > 0:
        max_y = max(Y)
    else:
        max_y = 0

    a = 0  # only_weak
    b = 0  # only_small
    c = 0  # either

    for i in range(T):
        w = W[i]
        s = S[i]
        can_weak = False
        can_small = False
        if A > 0:
            if w < max_x:
                can_weak = True
        if B > 0:
       