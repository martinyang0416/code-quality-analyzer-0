def minRemoveToMakeValid(s):
    stack = []
    remove = set()
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        elif c == ')':
            if stack:
                stack.pop()
            else:
                remove.add(i)
    # Add remaining unmatched '(' indices to remove set
    remove.update(stack)
    # Build the result string
    return ''.join([c for i, c in enumerate(s) if i not in remove])