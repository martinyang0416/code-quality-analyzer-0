import sys
from collections import defaultdict

def main():
    n = int(sys.stdin.readline())
    vendors = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    f1 = list(map(int, sys.stdin.readline().split()))
    f2 = list(map(int, sys.stdin.readline().split()))
    
    first_counts = defaultdict(int)
    second_total = defaultdict(int)
    
    for j in range(m):
        a = f1[j]
        b = f2[j]
        first_counts[a] += 1
        if a != b:
            seco