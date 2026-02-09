t = int(input())
for _ in range(t):
    n = int(input())
    max_b = n // 12
    found = False
    for b in range(max_b, -1, -1):
        remainder = n - 12 * b
        if remainder >= 0 and remainder % 10 == 0:
            a = remainder // 10
            print(a + b)
            found = True
            break
    if not found:
        print(-1)