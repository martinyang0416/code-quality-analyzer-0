import sys
import bisect

def main():
    N = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    prefix = [0] * (N + 1)
    for i in range(N):
        prefix[i+1] = prefix[i] + a[i]
    
    all_subarrays = []
    for l in range(N):
        for r in range(l, N):
            s = prefix[r+1] - prefix[l]
            all_subarrays.append((s, l, r))
    
    for i in range(N):
        a_list = []
        b_list = []
        for s, l, r in all_subarrays:
            if 