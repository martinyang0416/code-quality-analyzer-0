n = int(input())
patterns = []
for _ in range(n):
    parts = input().split()
    pattern = parts[0]
    security = int(parts[1])
    patterns.append((pattern, security))

m = int(input())
for _ in range(m):
    password = input().strip()
    max_security = 0
    for patt, sec in patterns:
        if len(patt) != len(password):
            continue
        match = True
        for i in range(len(patt)):
            if patt[i] == '*':
                continue
            if patt[i] != password[i]