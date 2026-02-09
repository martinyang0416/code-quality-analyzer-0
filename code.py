def putaway(A, B, T, X, Y, W, S):
    can_weak = [False] * T
    can_small = [False] * T

    for i in range(T):
        # Check can_weak[i]
        for x in X:
            if x > W[i]:
                can_weak[i] = True
                break
        # Check can_small[i]
        for y in Y:
            if y > S[i]:
                can_small[i] = True
                break

    # Check if any toy cannot be handled by any robot
    for i in range(T):
        if not (can_weak[i] or can_small[i]):
 