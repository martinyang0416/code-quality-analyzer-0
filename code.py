s = input().strip()
n = len(s)
if n % 2 == 0:
    all_even = True
    for c in s:
        if int(c) % 2 != 0:
            all_even = False
            break
    print("Yes" if all_even else "No")
else:
    mid = n // 2
    mid_digit = int(s[mid])
    print("Yes" if mid_digit % 2 == 1 else "No")