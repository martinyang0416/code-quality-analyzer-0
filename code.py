import sys

def main():
    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx])
    idx +=1
    for _ in range(T):
        N, K = int(input[idx]), int(input[idx+1])
        idx +=2
        S = list(map(int, input[idx:idx+N]))
        idx +=N
        mask = 1
        for num in S:
            if num == 0 or num > K:
                continue
            mask |= mask << num
            mask &= (1 << (K+1)) -1  # Keep only up to K bits
        if mask & (1 << K):
            print(1