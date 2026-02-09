t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    first_gt = s.find('>')
    last_lt = s.rfind('<')
    left = first_gt if first_gt != -1 else float('inf')
    right = (n - 1 - last_lt) if last_lt != -1 else float('inf')
    print(min(left, right))