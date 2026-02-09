k = int(input())
numbers = list(map(int, input().split()))
zero_present = 0 in numbers
non_zero = [x for x in numbers if x != 0]

def get_mask(n):
    mask = 0
    pos = 0
    while n > 0:
        digit = n % 10
        if digit != 0:
            mask |= (1 << pos)
        n = n // 10
        pos += 1
    return mask

masks = [get_mask(num) for num in non_zero]

# DP: mask -> (count, list)
dp = {0: (0, [])}
for i in range(len(non_zero)):
    num = non_zero[i]
    mask = masks[i]
    current_mask