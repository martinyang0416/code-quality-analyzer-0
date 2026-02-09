def isRobotBounded(instructions):
    # Directions: north, east, south, west
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    x, y = 0, 0
    current_dir = 0  # starts facing north
    
    for c in instructions:
        if c == 'G':
            dx, dy = dirs[current_dir]
            x += dx
            y += dy
        elif c == 'L':
            current_dir = (current_dir - 1) % 4
        elif c == 'R':
            current_dir = (current_dir + 1) % 4
    
    # Check if back to origin or direct