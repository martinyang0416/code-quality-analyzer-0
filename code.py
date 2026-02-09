a = int(input())
sum_digits = (a // 10) + (a % 10)
print("YES" if sum_digits == 5 or sum_digits == 10 else "NO")