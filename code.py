n = int(input())
distances = list(map(int, input().split()))
total = sum(distances)
target = total / 2

current_sum = 0
for i in range(n):
    current_sum += distances[i]
    if current_sum >= target:
        print(i + 1)
        break