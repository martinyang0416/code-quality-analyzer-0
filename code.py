import itertools

while True:
    n, k, s = map(int, input().split())
    if n == 0 and k == 0 and s == 0:
        break
    if k > n or k == 0:
        print(0)
        continue
    min_sum = k * (k + 1) // 2
    max_sum = k * (2 * n - k + 1) // 2
    if s < min_sum or s > max_sum:
        print(0)
        continue
    count = 0
    for comb in itertools.combinations(range(1, n + 1), k):
        if sum(comb) == s:
            count += 1
    print(count)