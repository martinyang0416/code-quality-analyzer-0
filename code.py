import bisect
import sys

def main():
    sys.setrecursionlimit(1 << 25)
    N, Q = map(int, sys.stdin.readline().split())
    s = sys.stdin.readline().strip()
    spec = sys.stdin.readline().strip()

    # Read L and R positions
    L_pos = []
    R_pos = []
    for idx in range(len(s)):
        if s[idx] == 'L':
            L_pos.append(idx + 1)  # 1-based
        else:
            R_pos.append(idx + 1)

    # Compute ℓ and r arrays (1-based)
    ell = [0] * (N + 1)
    r = [0] * (N + 1)
    f