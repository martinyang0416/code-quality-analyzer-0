import sys
from collections import defaultdict

def main():
    input = sys.stdin.read().split()
    ptr = 0
    T = int(input[ptr])
    ptr += 1
    for _ in range(T):
        n = int(input[ptr])
        m = int(input[ptr+1])
        ptr +=2
        if m == 0:
            print(0)
            ptr += 2*m
            continue
        adj = defaultdict(set)
        edges = []
        for __ in range(m):
            u = int(input[ptr])
            v = int(input[ptr+1])
            ptr +=2
         