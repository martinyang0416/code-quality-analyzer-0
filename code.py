# Read the number of test cases
t = int(input())
for _ in range(t):
    # Read K, L, E
    k, l, e = map(int, input().split())
    # Read friends' ages
    friends = list(map(int, input().split()))
    total = e + sum(friends)
    if l % total == 0:
        print("YES")
    else:
        print("NO")