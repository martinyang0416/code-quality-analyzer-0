def max_jumps(arr, d):
    n = len(arr)
    dp = [1] * n
    indices = sorted([(arr[i], i) for i in range(n)], key=lambda x: (x[0], x[1]))
    
    for a, i in indices:
        possible_js = []
        
        # Check left direction
        current_max = 0
        for x in range(1, min(d, i) + 1):
            j = i - x
            if j < 0:
                break
            if arr[j] >= arr[i]:
                break
            if x > 1:
                new_element = arr[j + 1]
                