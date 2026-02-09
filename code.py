n = int(input())
digits = list(map(int, input().split()))
allowed = set(digits)

all_abc = []
for a in digits:
    for b in digits:
        for c in digits:
            all_abc.append(a * 100 + b * 10 + c)

all_de = []
for d in digits:
    for e in digits:
        all_de.append(d * 10 + e)

solutions = 0

for abc in all_abc:
    for de in all_de:
        d_val = de // 10
        e_val = de % 10
        partial1 = abc * e_val
        if not (100 <= partial1 <= 999):
            continue
        i