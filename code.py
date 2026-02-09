import sys
import itertools

def main():
    C, N = map(int, sys.stdin.readline().split())
    masks = []
    mask_set = set()
    for _ in range(N):
        s = sys.stdin.readline().strip()
        mask = 0
        for i in range(C):
            if s[i] == 'G':
                mask |= 1 << (C - 1 - i)
        masks.append(mask)
        mask_set.add(mask)
    
    for a in masks:
        opposite = (~a) & ((1 << C) - 1)
        if opposite in mask_set:
            print(C)
            continue
 