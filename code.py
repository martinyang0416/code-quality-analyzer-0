def is_power_of_two(n):
    return (n & (n - 1)) == 0 and n != 0

a = int(input())
bits = a.bit_length()
if is_power_of_two(a):
    print(bits - 1)
else:
    print(bits)