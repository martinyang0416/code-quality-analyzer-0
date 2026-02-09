def putaway(A, B, T, X, Y, W, S):
    count_a = 0
    count_b = 0
    count_c = 0
    eligible_w = []
    eligible_s = []

    # Classify each toy into count_a, count_b, count_c, and collect eligible weights and sizes
    for i in range(T):
        w = W[i]
        s = S[i]
        eligibleW = any(w < x for x in X) if A > 0 else False
        eligibleS = any(s < y for y in Y) if B > 0 else False

        if not eligibleW and not eligibleS:
            return -1

        if eligibleW and eligible