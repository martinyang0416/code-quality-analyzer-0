import bisect

def main():
    import sys
    input = sys.stdin.read().split()
    n = int(input[0])
    a = list(map(int, input[1:n+1]))
    
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i+1] = prefix[i] + a[i]
    
    subarrays = []
    for s in range(1, n+1):
        for e in range(s, n+1):
            val = prefix[e] - prefix[s-1]
            subarrays.append( (s, e, val) )
    
    for i in range(1, n+1):
        S = []
        T = []
        for (s, e, val) in subarray