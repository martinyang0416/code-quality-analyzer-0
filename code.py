import sys
from collections import deque

def rotate_right(s, n):
    last_bit = s & 1
    s = (s >> 1) | (last_bit << (n - 1))
    return s

def main():
    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    N = int(input[idx])
    idx += 1

    for _ in range(T):
        lights_str = input[idx].strip()
        switches_str = input[idx+1].strip()
        idx += 2

        # Reverse to treat as little-endian (LSB is first character of string)
        lights_str