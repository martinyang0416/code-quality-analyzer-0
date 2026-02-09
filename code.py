# Read the number of test cases
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    grid = []
    for _ in range(n):
        row = input().split()
        grid.append(row)
    count = 0
    # Iterate through all possible 2x2 top-left positions
    for i in range(n - 1):
        for j in range(m - 1):
            # Check the four cells for the diamond pattern
            if (grid[i][j] == '/' and
                grid[i][j+1] == '\\' and
                grid[i+1][j] == '\\