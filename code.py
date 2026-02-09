a1, a2, a3 = map(int, input().split())

if a3 == 1:
    print(a2)
else:
    print(a1 + a2 * (a3 - 1))