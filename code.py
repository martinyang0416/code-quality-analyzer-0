P, K = map(int, input().split())
participants = list(range(1, P + 1))
current = 0

while len(participants) > 1:
    idx = (current + K - 1) % len(participants)
    del participants[idx]
    current = idx % len(participants)

print(participants[0])