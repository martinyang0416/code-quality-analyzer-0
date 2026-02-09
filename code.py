# Read input and process cities and roads
n = int(input())
cities = input().split()
cities_set = set(cities)
m = int(input())
roads = {}
for _ in range(m):
    c1, c2, d = input().split()
    roads[(c1, c2)] = int(d)
t = int(input())
for _ in range(t):
    parts = input().split()
    k = int(parts[0])
    route = parts[1:]
    # Check all cities exist
    valid = True
    for city in route:
        if city not in cities_set:
            valid = False
            break
    if not valid:
        p