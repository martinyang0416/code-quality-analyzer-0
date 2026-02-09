x, y, z = map(int, input().split())
x1, y1, z1 = map(int, input().split())
a1, a2, a3, a4, a5, a6 = map(int, input().split())

total = 0

# Check X-axis faces
if x < 0:
    total += a1
elif x > x1:
    total += a2

# Check Y-axis faces
if y < 0:
    total += a3
elif y > y1:
    total += a4

# Check Z-axis faces
if z < 0:
    total += a5
elif z > z1:
    total += a6

print(total)