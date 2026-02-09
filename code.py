s = input().strip()
first_two = int(s[1:3])
third_digit = s[3]
if third_digit == '1':
    print(first_two - 1)
else:
    print(first_two)