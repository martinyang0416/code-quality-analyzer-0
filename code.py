n = int(input())
x, y = 0, 0
directions = []
for _ in range(n):
    a, b = map(int, input().split())
    new_x_plus = x + a
    new_y_plus = y + b
    d_plus = abs(new_x_plus) + abs(new_y_plus)
    new_x_minus = x - a
    new_y_minus = y - b
    d_minus = abs(new_x_minus) + abs(new_y_minus)
    if d_plus < d_minus:
        directions.append(1)
        x, y = new_x_plus, new_y_plus
    else:
        directions.append(-1)
        x, y = new_x_minus, new_y_minus
print(' '.join(map(str, directions))