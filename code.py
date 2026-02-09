n, f = map(int, input().split())
s = list(map(int, input().split()))
t = list(map(int, input().split()))

# Calculate Alice's score
alice_total = 0
alice_time = 0
for i in range(n):
    alice_time += t[i]
    alice_total += s[i] - f * alice_time

# Calculate Bob's score
bob_total = 0
bob_time = 0
for i in range(n-1, -1, -1):
    bob_time += t[i]
    bob_total += s[i] - f * bob_time

# Compare the totals
if alice_total > bob_total:
    print("Alice")
elif bob_total > alice_total:
    print("Bob")