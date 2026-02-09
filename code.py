s = input().strip()
open_count = s.count('(')
close_count = s.count(')')
hashtags = [i for i, c in enumerate(s) if c == '#']
k = len(hashtags)
if k == 0:
    print(-1)
    exit()

required = open_count - close_count
if required < k or open_count < close_count:
    print(-1)
    exit()

assignments = [1] * (k-1) + [required - (k-1)]
if assignments[-1] < 1:
    print(-1)
    exit()

current_assignment = 0
balance = 0
possible = True

for c in s:
    if c == '(':
        balance += 1
    elif c == 