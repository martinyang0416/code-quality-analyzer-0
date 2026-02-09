T = int(input())
for _ in range(T):
    prices = list(map(int, input().split()))
    s = input().strip()
    present = set(s)
    total = 0
    for i in range(26):
        if chr(ord('a') + i) not in present:
            total += prices[i]
    print(total)