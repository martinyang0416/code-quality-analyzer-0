n = int(input())
L = list(map(int, input().split()))
path = [0] + L + [0]

original = 0
for i in range(1, len(path)):
    original += abs(path[i] - path[i-1])

for i in range(1, n+1):
    pre = path[i-1]
    curr = path[i]
    next_val = path[i+1]
    a = abs(curr - pre)
    b = abs(next_val - curr)
    c = abs(next_val - pre)
    new_dist = original - a - b + c
    print(new_dist)