def putaway(A: int, B: int, T: int, X: list, Y: list, W: list, S: list) -> int:
    max_X = -float('inf') if A == 0 else max(X)
    max_Y = -float('inf') if B == 0 else max(Y)

    toys = [(W[0], S[0]), (W[1], S[1])]
    possible = []

    for w, s in toys:
        can_weak = (max_X > w) if (A != 0) else False
        can_small = (max_Y > s) if (B != 0) else False

        allowed = []
        if can_weak:
            allowed.append('W')
        if can_small:
            allowed.append('S')

   