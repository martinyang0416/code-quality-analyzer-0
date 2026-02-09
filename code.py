import math

def find_max_subarray_with_gcd_one():
    T = int(input())
    for _ in range(T):
        N = int(input())
        arr = list(map(int, input().split()))
        max_length = -1
        previous_gcds = {}
        
        for num in arr:
            current_gcds = {}
            # Consider the current number alone
            current_gcds[num] = 1
            
            # Process each GCD from the previous step
            for g in previous_gcds:
                new_gcd = math.gcd(