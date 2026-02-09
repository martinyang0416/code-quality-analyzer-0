def baseNeg2(N):
    if N == 0:
        return "0"
    res = []
    while N != 0:
        remainder = N % (-2)
        N = N // (-2)
        if remainder < 0:
            remainder += 2
            N += 1
        res.append(str(remainder))
    return ''.join(reversed(res))