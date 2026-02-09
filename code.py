import sys
from collections import deque

def rotate_right(s, N):
    last_bit = s & 1
    s = (s >> 1)
    return s | (last_bit << (N - 1))

def main():
    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    N = int(input[idx])
    idx += 1

    for _ in range(T):
        L_str = input[idx]
        S_str = input[idx+1]
        idx += 2

        # Convert strings to integers (bitmasks)
        L = 0
        S = 0
        for i in range(N):
            bit_L = i