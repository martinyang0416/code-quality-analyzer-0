def main():
    import sys
    N, M = map(int, sys.stdin.readline().split())
    
    # Calculate the number of set bits (minimum terms)
    K = bin(N).count('1')
    
    if M < K:
        print("NO")
        return
    
    # Calculate the maximum possible terms by splitting each set bit completely.
    max_terms = 0
    temp = N
    exp = 0
    while temp > 0:
        if temp & 1:
            max_terms += 2 ** exp
        exp += 1
        temp >>= 1
    
    if M <= max_terms:
        print("