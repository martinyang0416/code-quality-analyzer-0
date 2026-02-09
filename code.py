n = int(input())
s = input().strip()
q = int(input())

# Precompute for each character
pre = {}

for c in 'abcdefghijklmnopqrstuvwxyz':
    B = []
    for i in range(n):
        if s[i] != c:
            B.append(i)
    len_b = len(B)
    best = [0] * (n + 1)
    for m in range(n + 1):
        if m >= len_b:
            best[m] = n
        else:
            max_len = 0
            # Iterate through possible windows
            for i in range(len_b - m + 1):
                if i > 0:
            