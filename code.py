def monotoneIncreasingDigits(N):
    digits = list(str(N))
    n = len(digits)
    i = 0
    # Find the first index where digits[i] > digits[i+1]
    while i < n - 1 and digits[i] <= digits[i + 1]:
        i += 1
    if i == n - 1:
        return int(''.join(digits))
    # Backtrack to the left for equal digits
    while i > 0 and digits[i - 1] == digits[i]:
        i -= 1
    # Decrease the current digit and set the rest to '9'
    digits[i] = str(int(digits[i]) - 1)
    for j in range(i + 1, n