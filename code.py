a = int(input())
sum_digits = sum(int(d) for d in str(a))
print("YES" if sum_digits % 5 == 0 else "NO")