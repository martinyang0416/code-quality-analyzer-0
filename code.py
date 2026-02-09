n = int(input())

even = []
odd = []

for num in range(1, n * n + 1):
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

matrix = []
e_ptr = 0
o_ptr = 0

for i in range(n):
    if i % 2 == 0:
        row = []
        for j in range(n // 2):
            row.append(even[e_ptr])
            e_ptr += 1
        for j in range(n // 2):
            row.append(even[e_ptr])
            e_ptr += 1
        matrix.append(row)
    else:
        row = []
        for j in range(n 