s = input().strip()
last_digit = int(s[-1])
print(0 if last_digit % 2 == 0 else 1)