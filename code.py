def main():
    import sys
    n = int(sys.stdin.readline())
    b = list(map(int, sys.stdin.readline().split()))
    min_time = float('inf')
    ans = -1

    for s in range(n):
        current_b = b[s]
        if current_b <= s:
            current_time = s
        else:
            delta = current_b - s
            k = (delta + n - 1) // n  # ceiling(delta / n)
            current_time = s + k * n
        if current_time < min_time:
            min_time = current_time
            ans = s
    