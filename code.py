import sys

def main():
    N, K, T = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))
    T = T % N  # Reduce T using the periodicity

    current = list(range(N))  # current[pos] is the cow at position pos

    for step in range(T):
        active = [(A[i] + step) % N for i in range(K)]
        # Extract the cows in these active positions
        cows = [current[a] for a in active]
        # Rotate right by one: last element comes first
        rotate