s = input().strip()
zeros = s.count('0')
ones = len(s) - zeros
print(2 * min(zeros, ones))