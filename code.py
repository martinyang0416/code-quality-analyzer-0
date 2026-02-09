from collections import deque

def rotate_right(s, N):
    last_bit = s & 1
    rotated = (s >> 1) | (last_bit << (N - 1))
    return rotated

def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    N = int(input[idx])
    idx += 1
    for _ in range(T):
        L_str = input[idx]
        S_str = input[idx + 1]
        idx += 2
        L = int(L_str, 2)
        S = int(S_str, 2)
        visited = {}
        initial_key = (S << N) | L
 