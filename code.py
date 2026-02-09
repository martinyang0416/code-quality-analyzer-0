m, n = map(int, input().split())
k = int(input())
grid = [input().strip() for _ in range(m)]

prefix_j = [[0]*(n+1) for _ in range(m+1)]
prefix_o = [[0]*(n+1) for _ in range(m+1)]
prefix_i = [[0]*(n+1) for _ in range(m+1)]

for i in range(1, m+1):
    for j in range(1, n+1):
        current = grid[i-1][j-1]
        j_val = 1 if current == 'J' else 0
        o_val = 1 if current == 'O' else 0
        i_val = 1 if current == 'I' else 0
        
        prefix_j[i][j] = prefix_j[i-1][j] + prefix_j[