import bisect
import sys
import math

def main():
    A, B, T = map(int, sys.stdin.readline().split())
    X = list(map(int, sys.stdin.readline().split())) if A > 0 else []
    Y = list(map(int, sys.stdin.readline().split())) if B > 0 else []
    W = []
    S = []
    for _ in range(T):
        w, s = map(int, sys.stdin.readline().split())
        W.append(w)
        S.append(s)

    X.sort()
    Y.sort()

    count1 = 0  # must be handled by weak
    count2 = 0  # must be handled by small
    c