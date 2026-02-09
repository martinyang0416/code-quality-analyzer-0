import sys
from collections import defaultdict

def main():
    input = sys.stdin.read().split()
    ptr = 0
    T = int(input[ptr])
    ptr += 1
    for _ in range(T):
        N, K = int(input[ptr]), int(input[ptr+1])
        ptr +=2
        events = defaultdict(list)
        for _ in range(N):
            s = int(input[ptr])
            e = int(input[ptr+1])
            p = int(input[ptr+2])
            ptr +=3
            events[p].append((s, e))
        total = 0
        for room in events:
