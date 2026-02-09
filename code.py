def find_largest_number(Y):
    if Y % 2 != 0:
        return -1
    for s in range(Y, -1, -2):
        o = Y - s
        if o >= 0 and o % 4 == 0:
            return '7' * s + '1' * o
    return -1

T = int(input())
for _ in range(T):
    Y = int(input())
    result = find_largest_number(Y)
    print(result if result != -1 else -1)