n, x, y = map(int, input().split())
s = input().strip()

suffix = s[-x:]
target = ['0'] * x
target[x - y - 1] = '1'

count = 0
for i in range(x):
    if suffix[i] != target[i]:
        count += 1

print(count)