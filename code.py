n, k = map(int, input().split())
w_list = list(map(int, input().split()))
total_pockets = sum((w + k - 1) // k for w in w_list)
days = (total_pockets + 1) // 2
print(days)