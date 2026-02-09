a1, a2, a3 = map(int, input().split())
steps = a3 - 1
first, second = a1, a2
for _ in range(steps):
    next_term = first + second
    first, second = second, next_term
print(second)