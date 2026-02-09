import sys

def main():
    N = int(sys.stdin.readline())
    result = []
    for _ in range(N):
        parts = list(map(int, sys.stdin.readline().split()))
        a, b, c, d, e = parts
        S = a + b + c
        
        # Generate all triplets for S
        triplets = []
        for a1 in range(0, 3):
            for b1 in range(0, 3):
                for c1 in range(0, 3):
                    if a1 + b1 + c1 == S:
                        triplets.append((a1, b1, c1))
        # Sort the t