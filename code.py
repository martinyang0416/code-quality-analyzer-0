import sys

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        s = sys.stdin.readline().strip()
        n = len(s)
        if n == 0:
            print(0)
            continue
        prev_dp = {}
        # Initialize for the first character (i=0)
        for c in 'abcdefghijklmnopqrstuvwxyz':
            cost = 0 if c == s[0] else 1
            prev_dp[(None, c)] = cost
        # Process remaining characters
        for i in range(1, n):
            current_dp = {}
   