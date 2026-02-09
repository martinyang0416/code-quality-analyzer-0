def main():
    import itertools

    T = int(input())
    for _ in range(T):
        N, B = map(int, input().split())
        C = list(map(int, input().split()))
        H = list(map(int, input().split()))
        
        max_beauty = 0
        
        # Check all single flower types
        for i in range(N):
            if C[i] <= B:
                max_beauty = max(max_beauty, H[i])
        
        # Check all pairs
        for pair in itertools.combinations(range(N), 2):
            i, j