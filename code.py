import bisect

def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    N = int(input[ptr])
    ptr += 1
    a = list(map(int, input[ptr:ptr+N]))
    ptr += N
    Q = int(input[ptr])
    ptr += 1
    queries = []
    for _ in range(Q):
        i = int(input[ptr])
        j = int(input[ptr+1])
        queries.append((i, j))
        ptr += 2

    # Prepare the initial sorted array and prefix sums
    S = sorted(a, reverse=True)
    prefix = [0] * (N + 1)
    for i in range(N