import sys
from sys import stdin
from collections import defaultdict

def main():
    input = sys.stdin.read().split()
    ptr = 0
    T = int(input[ptr])
    ptr += 1
    for _ in range(T):
        N = int(input[ptr])
        ptr += 1
        edges = [[] for _ in range(N+1)]
        for _ in range(N-1):
            u = int(input[ptr])
            v = int(input[ptr+1])
            ptr += 2
            edges[u].append(v)
            edges[v].append(u)
        if (N-1) % 3 != 0:
            print(