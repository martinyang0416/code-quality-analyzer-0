n = int(input())
s = input().strip()

for i in range(n):
    if s[i] == '*':
        max_d = (n - 1 - i) // 4
        for d in range(1, max_d + 1):
            valid = True
            for k in range(5):
                pos = i + k * d
                if pos >= n or s[pos] != '*':
                    valid = False
                    break
            if valid:
                print("yes")
                exit()
print("no")