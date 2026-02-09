import bisect

def putaway(A, B, T, X, Y, W, S):
    if T == 0:
        return 0

    # Sort the X and Y arrays for efficient lookups
    sortedX = sorted(X) if A > 0 else []
    sortedY = sorted(Y) if B > 0 else []

    Ow_count = 0  # Toys that can only go to weak robots
    Os_count = 0  # Toys that can only go to small robots
    B_count = 0   # Toys that can go to either
    has_impossible = False

    for i in range(T):
        w = W[i]
        s = S[i]
        can_weak = False
        can