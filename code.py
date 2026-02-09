n, m = map(int, input().split())
rows = (1 << n) - 1
cols = (1 << m) - 1

for _ in range(rows):
    print('0' * cols)