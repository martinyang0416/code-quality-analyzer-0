def numOfSubarrays(arr, k, threshold):
    target = threshold * k
    n = len(arr)
    if n < k:
        return 0
    current_sum = sum(arr[:k])
    count = 1 if current_sum >= target else 0
    for i in range(k, n):
        current_sum += arr[i] - arr[i - k]
        if current_sum >= target:
            count += 1
    return count