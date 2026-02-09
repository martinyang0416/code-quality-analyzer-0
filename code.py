n, s_x, s_y = map(int, input().split())

east = 0
west = 0
north = 0
south = 0

for _ in range(n):
    x, y = map(int, input().split())
    if x > s_x:
        east += 1
    elif x < s_x:
        west += 1
    if y > s_y:
        north += 1
    elif y < s_y:
        south += 1

max_count = max(east, west, north, south)
directions = [
    (east, (s_x + 1, s_y)),
    (west, (s_x - 1, s_y)),
    (north, (s_x, s_y + 1)),
    (south, (s_x, s_y - 1)),
]

# Find the first direction with max_count and v