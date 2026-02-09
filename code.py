# Precompute the last digits of the first 60 Fibonacci numbers
fib_last_digits = [0] * 60
fib_last_digits[0] = 0
if len(fib_last_digits) > 1:
    fib_last_digits[1] = 1
    prev, curr = 0, 1
    for i in range(2, 60):
        next_val = (prev + curr) % 10
        fib_last_digits[i] = next_val
        prev, curr = curr, next_val

import sys

def main():
    input = sys.stdin.read
    data = input().split()
    T = int(data[0])
    for i in range(1, T+1):
        N = int(data[i])
        if N == 0