def minFlips(a, b, c):
    flips = 0
    for i in range(31):
        a_bit = (a >> i) & 1
        b_bit = (b >> i) & 1
        c_bit = (c >> i) & 1
        if (a_bit | b_bit) != c_bit:
            if c_bit == 1:
                flips += 1
            else:
                flips += a_bit + b_bit
    return flips