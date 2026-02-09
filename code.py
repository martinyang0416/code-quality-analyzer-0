import sys

def max_sum(t):
    k = (t + 1) // 2
    return k * (t - k + 1)

def find_min_time(N):
    low = 1
    high = N
    ans = N  # worst case is N seconds
    while low <= high:
        mid = (low + high) // 2
        current_max = max_sum(mid)
        if current_max >= N:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

def main():
    input = sys.stdin.read().split()
    T = int(input[0])
    idx = 1
    for _ in range(T):
       