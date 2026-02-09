import sys

def main():
    input = sys.stdin.read
    data = input().split()
    T = int(data[0])
    cases = data[1:T+1]
    for s in cases:
        N = len(s)
        forward = [1] * (N + 1)
        for i in range(1, N + 1):
            prev_char = s[i-1]
            if prev_char == '<':
                forward[i] = forward[i-1] + 1
            elif prev_char == '=':
                forward[i] = forward[i-1]
            else:
                forward[i] = 1
        backward = [1] * (N + 1)
   