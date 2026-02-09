n = int(input())
arr = list(map(int, input().split()))
stack = []
max_step = 0

for num in arr:
    current_step = 0
    while stack and stack[-1][0] < num:
        current_step = max(current_step, stack.pop()[1])
    if stack:
        current_step += 1
    else:
        current_step = 0
    stack.append((num, current_step))
    if current_step > max_step:
        max_step = current_step

print(max_step)