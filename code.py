s = input().strip()
digits = s[1:]  # Extract the six digits after 'A'
first_two = digits[:2]
x = int(first_two)
fourth_digit = digits[3]  # The fourth character in the digits (index 3)
if fourth_digit == '0':
    x -= 1
print(x)