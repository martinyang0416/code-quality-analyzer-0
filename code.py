import math

b, m = map(int, input().split())
e = b + m - 1

k = math.ceil(math.sqrt(b))
l = math.floor(math.sqrt(e))

if l < k:
    print(0)
else:
    print(l - k + 1)