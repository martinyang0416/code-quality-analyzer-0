def calculate(s):
    stack = []
    current_num = 0
    current_operator = '+'
    
    for c in s:
        if c.isdigit():
            current_num = current_num * 10 + int(c)
        elif c in '+-*/':
            if current_operator == '+':
                stack.append(current_num)
            elif current_operator == '-':
                stack.append(-current_num)
            elif current_operator == '*':
                stack.append(stack.pop() * current_num)
            elif current_operato