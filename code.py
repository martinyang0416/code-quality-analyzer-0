import sys
MOD = 10**9 + 7

def main():
    N, M = map(int, sys.stdin.readline().split())
    masks = []
    for _ in range(M):
        s = sys.stdin.readline().strip()
        masks.append(s)
    
    # Create bitmask for each problem
    problem_masks = []
    for i in range(N):
        bm = 0
        for m in range(M):
            if masks[m][i] == 'E':
                bm |= (1 << m)
        problem_masks.append(bm)
    
    # Group by masks
    from collections import defaultdict
    count =