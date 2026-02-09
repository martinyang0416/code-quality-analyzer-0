k = int(input())
nums = list(map(int, input().split()))

s = {0}
for num in nums:
    for current in list(s):
        s.add(current + num)

print(len(s))