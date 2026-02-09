t = int(input())
for _ in range(t):
    s = input().strip()
    w_pos = s.index('W')
    left = s[:w_pos].count('B')
    right = s[w_pos+1:].count('B')
    if left != right:
        print("Aleksa")
    else:
        print("Chef")