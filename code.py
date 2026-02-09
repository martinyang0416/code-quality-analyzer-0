import sys

def main():
    input = sys.stdin.read().split()
    ptr = 0
    T = int(input[ptr])
    ptr += 1
    for _ in range(T):
        N, K = map(int, input[ptr:ptr+2])
        ptr += 2
        A = list(map(int, input[ptr:ptr+N]))
        ptr += N
        
        # Compute max_single using Kadane's algorithm
        max_current = max_global = A[0]
        for num in A[1:]:
            max_current = max(num, max_current + num)
            max_global = max(max_global, max_current)
        m