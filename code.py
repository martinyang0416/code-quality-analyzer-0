def numTeams(rating):
    n = len(rating)
    total = 0
    for j in range(1, n - 1):
        left_small = left_large = 0
        for i in range(j):
            if rating[i] < rating[j]:
                left_small += 1
            elif rating[i] > rating[j]:
                left_large += 1
        
        right_small = right_large = 0
        for k in range(j + 1, n):
            if rating[k] < rating[j]:
                right_small += 1
            elif rating[k] > rating[j]:
                r