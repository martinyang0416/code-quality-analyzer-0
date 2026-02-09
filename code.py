import sys

def main():
    import bisect
    N = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    prefix = [0] * (N + 1)
    for i in range(N):
        prefix[i+1] = prefix[i] + a[i]

    subarrays = []
    for start in range(N):
        for end in range(start, N):
            s = prefix[end+1] - prefix[start]
            subarrays.append( (s, start, end) )

    for i in range(N):
        S = []
        T = []
        for (s_val, s_start, s_end) in subarrays:
 