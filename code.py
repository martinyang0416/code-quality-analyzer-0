def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    for _ in range(T):
        N, K = map(int, input[idx:idx+2])
        idx +=2
        A = list(map(int, input[idx:idx+N]))
        idx += N
        
        # Compute inv_A: inversions in original array
        inv_A = 0
        for i in range(N):
            for j in range(i+1, N):
                if A[i] > A[j]:
                    inv_A += 1
        
        # Compute cross_pair