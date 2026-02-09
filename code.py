from collections import defaultdict

def findLatestStep(arr, m):
    n = len(arr)
    if m > n:
        return -1
    left_end = dict()
    right_start = dict()
    freq = defaultdict(int)
    ans = -1
    for i in range(n):
        x = arr[i]
        new_start = x
        new_end = x
        
        # Check left neighbor
        if (x - 1) in right_start:
            left_group_start = right_start[x - 1]
            left_group_end = x - 1
            len_left = left_group_end - left_group_star