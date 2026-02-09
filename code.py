import sys

def main():
    input = sys.stdin.read().split()
    ptr = 0
    T = int(input[ptr])
    ptr += 1
    for _ in range(T):
        N = int(input[ptr])
        ptr += 1
        arr = list(map(int, input[ptr:ptr+N]))
        ptr += N
        max_len = 2
        for i in range(N-1):
            a = arr[i]
            b = arr[i+1]
            current_len = 2
            next_idx = i + 2
            while next_idx < N:
                expected = a + b
                if arr[next_idx] == exp