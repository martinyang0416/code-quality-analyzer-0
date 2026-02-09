import math

def compute_gcd(arr):
    current_gcd = arr[0]
    for num in arr[1:]:
        current_gcd = math.gcd(current_gcd, num)
        if current_gcd == 1:
            break
    return current_gcd

def main():
    import sys
    input = sys.stdin.read().split()
    n = int(input[0])
    a = list(map(int, input[1:n+1]))
    
    if n == 0:
        print(0)
        return
    
    g = compute_gcd(a)
    
    b = [num // g for num in a]
    
    if len(b) < 2:
        print(0)
        return
