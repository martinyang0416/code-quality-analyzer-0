from collections import defaultdict

s = input().strip()
counts = defaultdict(int)
month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(len(s) - 9):
    substring = s[i:i+10]
    if substring[2] != '-' or substring[5] != '-':
        continue
    day_part = substring[:2]
    month_part = substring[3:5]
    year_part = substring[6:10]
    if not (day_part.isdigit() and month_part.isdigit() and year_part.isdigit()):
        continue
    day = int(day_part)
    month = int(