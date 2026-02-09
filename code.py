def putaway(A, B, T, X, Y, W, S):
    # Precompute eligibility for each toy
    toys_w_ok = [False] * T
    toys_s_ok = [False] * T

    for i in range(T):
        w = W[i]
        s = S[i]

        # Check weak eligibility
        w_ok = False
        for x in X:
            if w < x:
                w_ok = True
                break
        # Check small eligibility
        s_ok = False
        for y in Y:
            if s < y:
                s_ok = True
                break

        toys_w_