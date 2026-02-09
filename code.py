def convert_to_base(n, k):
    if n == 0:
        return '0'
    digits = []
    while n > 0:
        digits.append(str(n % k))
        n = n // k
    return ''.join(reversed(digits))

k = int(input())

for i in range(1, k):
    row = []
    for j in range(1, k):
        product = i * j
        row.append(convert_to_base(product, k))
    print(' '.join(row))