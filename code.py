import sys

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        arr = list(map(int, sys.stdin.readline().split()))
        if n <= 2:
            print(n)
            continue
        max_len = 2
        for i in range(n - 1):
            a = arr[i]
            b = arr[i+1]
            current_len = 2
            j = i + 2
            while j < n:
                c = a + b
                if arr[j] == c:
                    current_l