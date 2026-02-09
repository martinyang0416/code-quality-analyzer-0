n, m = map(int, input().split())
cyclic = [input().strip() for _ in range(n)]
r, c = map(int, input().split())
pattern = [input().strip() for _ in range(r)]

constraints = []
for x in range(r):
    for y in range(c):
        v = pattern[x][y]
        if v != '?':
            constraints.append((x, y, v))

if not constraints:
    for _ in range(n):
        print('1' * m)
    exit()

result = [[1]*m for _ in range(n)]

for dx, dy, v in constraints:
    mask = [[0]*m for _ in range(n)]
    for i in