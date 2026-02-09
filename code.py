def minimal_array_length(test_cases):
    for case in test_cases:
        n, a = case
        stack = []
        for num in a:
            stack.append(num)
            while len(stack) >= 3:
                if stack[-3] == stack[-1]:
                    s = stack.pop()
                    stack.pop()
                    stack[-1] += s
                else:
                    break
        print(len(stack))

# Reading input
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input()