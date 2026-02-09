a, b = map(int, input().split())

def minimal_capacitors(a, b):
    sum_q = 0
    while b != 0:
        sum_q += a // b
        a, b = b, a % b
    return sum_q

print(minimal_capacitors(a, b))