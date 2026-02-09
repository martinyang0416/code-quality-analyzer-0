n = int(input())
a = list(map(int, input().split()))
unique_a = set(a)
print(sum(unique_a))