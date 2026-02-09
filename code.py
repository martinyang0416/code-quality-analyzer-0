target, n = map(int, input().split())

# Calculate the sum of squares from 1 to n
sum_squares = n * (n + 1) * (2 * n + 1) // 6

if target > sum_squares:
    print(-1)
else:
    remaining = target
    result = []
    for i in range(n, 0, -1):
        square = i * i
        if square <= remaining:
            result.append(i)
            remaining -= square
            if remaining == 0:
                break
    if remaining != 0:
        print(-1)
    else:
        print(len(result))
        pri