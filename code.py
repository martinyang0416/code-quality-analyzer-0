def main():
    import sys
    input = sys.stdin.read().split()
    M = int(input[0])
    arr = list(map(int, input[1:M+1]))
    arr.sort()
    
    # Case 1: R is max, S is min. P and Q are second and third max.
    case1 = (arr[-2] + arr[-3]) * (arr[-1] - arr[0])
    
    # Case 2: R is second max, S is min. P and Q are max and third max.
    case2 = (arr[-1] + arr[-3]) * (arr[-2] - arr[0])
    
    # Case 3: R is max, S is min. P and Q are max and second max.
    case3 = (arr[-1] + arr[-2]) *