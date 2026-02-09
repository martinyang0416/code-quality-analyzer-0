t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    for _ in range(b):
        input()  # consume the driver routes, not needed for the solution
    print(a - 1)