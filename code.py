T = int(input())
for _ in range(T):
    s = input().strip()
    stack = []
    valid = True
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if not stack:
                valid = False
                break
            stack.pop()
    if valid and not stack:
        print("YES")
    else:
        print("NO")