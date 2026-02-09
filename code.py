n = int(input())
s = input().strip()

first_r = s.find('R')

if first_r == -1:
    count = s.count('U')
else:
    count = s[:first_r].count('U')

print(count)