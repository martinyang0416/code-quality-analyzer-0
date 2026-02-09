def rotate_right(s, N):
    last_bit = s & 1
    s >>= 1
    s |= last_bit << (N - 1)
    return s

def solve():
    import sys
    from collections import deque

    T, N = map(int, sys.stdin.readline().split())
    for _ in range(T):
        L_str, S_str = sys.stdin.readline().strip().split()
        L0 = int(L_str, 2)
        S0 = int(S_str, 2)
        desired = L0

        found = False
        result = -1

        # BFS using level by level steps
        initial = (S0, 0)
        visited = 