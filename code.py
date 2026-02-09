def generate_spiral(n):
    grid = [['.' for _ in range(n)] for _ in range(n)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dir_idx = 0
    steps = [n//2, n//2 -1]
    row, col = n//2 -1, n//2 -1
    if n % 2 != 0:
        return None
    count = 0
    grid[row][col] = 'E'
    count +=1
    while True:
        for _ in range(2):
            step = steps[dir_idx%2]
            if step <=0:
                return grid
            for __ in range(step):
                dr, dc = direction