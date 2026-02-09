t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    p = [0] * n
    p[0] = a[0]
    for i in range(1, n-1):
        options = [a[i], b[i], c[i]]
        for opt in options:
            if opt != p[i-1]:
                p[i] = opt
                break
    # Handle last element
    i = n-1
    options = [a[i], b[i], c[i]]
    candidates = [x for x in options if x != p[i