s = input().strip()
n = len(s)
values = [ord(c) - ord('A') + 1 for c in s]

valid = True
for i in range(n // 2):
    if (values[i] + values[n - 1 - i]) % 2 != 0:
        valid = False
        break

if valid and n % 2 == 1:
    mid = values[n // 2]
    if mid % 2 != 0:
        valid = False

print("YES" if valid else "NO")