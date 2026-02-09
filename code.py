n, m = map(int, input().split())
board = [list(map(int, list(input().strip()))) for _ in range(n)]

# Precompute p1 and p2 matrices
p1 = [[0] * m for _ in range(n)]
p2 = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        expected_p1 = (i + j) % 2
        p1[i][j] = 1 if (board[i][j] == expected_p1) else 0
        expected_p2 = 1 - expected_p1
        p2[i][j] = 1 if (board[i][j] == expected_p2) else 0

# Compute prefix sums for p1 and p2
sum_p1 = [[0] * (m + 1) for _ i