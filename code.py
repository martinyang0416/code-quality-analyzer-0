n = int(input())
if n == 0:
    print(0)
    exit()

positions = {0: (0, 0)}

for i in range(1, n):
    parent, direction = map(int, input().split())
    x, y = positions[parent]
    if direction == 0:  # left
        new_x = x - 1
        new_y = y
    elif direction == 1:  # down
        new_x = x
        new_y = y - 1
    elif direction == 2:  # right
        new_x = x + 1
        new_y = y
    else:  # up (direction 3)
        new_x = x
        new_y = y + 1
    positions[i] = (new_x, new_y)