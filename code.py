def largestMultipleOfThree(digits):
    digits_sorted = sorted(digits, reverse=True)
    sum_total = sum(digits_sorted)
    rem = sum_total % 3
    
    if rem == 0:
        if not digits_sorted:
            return ""
        if digits_sorted[0] == 0:
            return "0"
        return ''.join(map(str, digits_sorted))
    else:
        candidate = []
        if rem == 1:
            # Try to remove one mod 1 digit
            found = -1
            for i in range(len(digits_sorted)-1, -1, -1)