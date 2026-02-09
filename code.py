t = input().strip()
result = []
for char in t:
    if char == 'A':
        result.append('A')
    elif char == 'B':
        result.append('B')
    elif char == 'D':
        if result:
            result.pop()
print(''.join(result))