import math

def main():
    n = int(input())
    nums = [int(input()) for _ in range(n)]
    
    non_zero = [x for x in nums if x != 0]
    zeros = [x for x in nums if x == 0]
    
    # Custom key function for sorting
    def sort_key(x):
        if x == 0:
            return (0, x)  # Not used here since non_zero has no zeros
        return (-(math.log(x) / x), x)
    
    # Sort the non-zero elements
    non_zero_sorted = sorted(non_zero, key=sort_key)
    
    # Combine and output
    resu