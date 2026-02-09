import sys
from collections import defaultdict

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        a = list(map(int, sys.stdin.readline().split()))
        d = defaultdict(set)
        found = False
        for x in a:
            mapped_val = a[x-1]
            d[mapped_val].add(x)
            if len(d[mapped_val]) >= 2:
                found = True
                break
        print("Truly Happy" if found else "Poor Chef")

if __