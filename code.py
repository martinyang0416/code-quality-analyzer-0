import sys
MOD = 10**9 + 7

def main():
    N, M = map(int, sys.stdin.readline().split())
    masks = []
    for _ in range(M):
        s = sys.stdin.readline().strip()
        masks.append(s)
    
    problem_masks = []
    for i in range(N):
        current_mask = 0
        for m in range(M):
            if masks[m][i] == 'H':
                current_mask |= 1 << m
        problem_masks.append(current_mask)
    
    from collections import defaultdict
    cnt = defaultdict(int)
    for m in pr