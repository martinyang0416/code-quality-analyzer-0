def count_even_squares(N):
    if N < 2:
        return 0
    max_s = N if N % 2 == 0 else N - 1
    if max_s < 2:
        return 0
    total = 0
    for s in range(2, max_s + 1, 2):
        step = (N - s) // 2
        total += (step + 1) ** 2
    return total

T = int(input())
for _ in range(T):
    N = int(input())
    print(count_even_squares(N))