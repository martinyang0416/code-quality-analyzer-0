import sys

def main():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N, R = map(int, input().split())
        canonical_map = {}
        scores = {}
        # Process first R submissions (registered teams)
        for _ in range(R):
            parts = input().strip().split()
            ti = ' '.join(parts[:-1])
            pi = int(parts[-1])
            canonical = ''.join(sorted(ti))
            canonical_map[canonical] = ti
            scores[ti] = scor