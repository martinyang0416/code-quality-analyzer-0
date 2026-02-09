a, b, c = map(int, input().split())
for x in range(c // a + 1):
    remainder = c - a * x
    if remainder >= 0 and remainder % b == 0:
        print("Yes")
        exit()
print("No")