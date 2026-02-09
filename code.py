import bisect

def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    N = int(input[ptr])
    ptr += 1
    a = list(map(int, input[ptr:ptr+N]))
    ptr += N
    S = sorted(a)
    prefix = [0] * (N + 1)
    for i in range(N):
        prefix[i + 1] = prefix[i] + S[i]
    T = 0
    for i in range(N):
        T += S[i] * (i + 1)
    Q = int(input[ptr])
    ptr += 1
    for _ in range(Q):
        i = int(input[ptr]) - 1  # Convert to 0-based index
        j = int(input[ptr + 