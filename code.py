import sys

def solve():
    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    for _ in range(T):
        N = int(input[idx])
        K = int(input[idx+1])
        M = int(input[idx+2])
        X0 = int(input[idx+3])  # not used
        idx +=4
        
        if K == 1:
            if M == N:
                print("yes")
            else:
                print("no")
            continue
        
        possible = False
        for c0 in [0, 1]:
            