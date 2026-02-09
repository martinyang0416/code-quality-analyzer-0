n, *rest = map(int, open(0).read().split())
a = rest[:n]
print(sum(x - 1 for x in a))