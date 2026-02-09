s = input().strip()
digits = list(map(int, s[1:]))
sum_d = sum(digits)
has_zero = 0 in digits
if has_zero:
    print(sum_d + 10)
else:
    print(sum_d + 1)