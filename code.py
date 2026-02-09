import sys

def main():
    input = sys.stdin.read().split()
    ptr = 0
    N = int(input[ptr])
    ptr += 1
    Q = int(input[ptr])
    ptr += 1
    a = list(map(int, input[ptr:ptr+N]))
    ptr += N
    
    pre_sum = [0] * (N + 1)
    for i in range(1, N + 1):
        pre_sum[i] = pre_sum[i-1] + a[i-1]
    
    for _ in range(Q):
        L = int(input[ptr])
        ptr += 1
        R = int(input[ptr])
        ptr += 1
        
        sum_res = pre_sum[R] - pre_sum[L-1]
        if L == R:
   