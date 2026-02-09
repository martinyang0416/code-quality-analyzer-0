import sys
from itertools import combinations

def main():
    C, N = map(int, sys.stdin.readline().split())
    masks = []
    mask_set = set()

    for _ in range(N):
        s = sys.stdin.readline().strip()
        mask = 0
        for c in s:
            mask = (mask << 1) | (1 if c == 'H' else 0)
        masks.append(mask)
        mask_set.add(mask)

    max_distances = []

    for a in masks:
        complement = ((1 << C) - 1) ^ a
        if complement in mask_set:
            max_distanc