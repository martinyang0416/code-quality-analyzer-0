n = int(input())
total = 0.0
for m in range(1, n + 1):
    if m == 1:
        denom = 1
    else:
        denom = 3 * m - 1
    total += 2 / denom
rounded_total = round(total, 2)
print("{0:.2f}".format(rounded_total))