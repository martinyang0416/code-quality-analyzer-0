T = int(input())
for _ in range(T):
    N = int(input())
    for i in range(1, N + 1):
        numbers = list(range(1, i + 1))
        line = ' '.join(map(str, numbers))
        print(line)