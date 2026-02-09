n = int(input())
recipients = list(map(int, input().split()))
counts = [0] * (n + 1)

for r in recipients:
    counts[r] += 1

print(' '.join(map(str, counts[1:n+1])))