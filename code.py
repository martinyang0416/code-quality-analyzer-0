def findBestValue(arr, target):
    sum_arr = sum(arr)
    if sum_arr <= target:
        return max(arr)
    
    arr_sorted = sorted(arr)
    n = len(arr_sorted)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i+1] = prefix[i] + arr_sorted[i]
    
    best_x = None
    best_diff = float('inf')
    
    # Handle x < arr_sorted[0]
    if arr_sorted:
        a = 0
        b = arr_sorted[0]
        B = n
        if B > 0:
            x_opt_floor = target // B
            x_opt_ceil