def maxScore(cardPoints, k):
    n = len(cardPoints)
    prefix = [0]
    current_sum = 0
    for i in range(k):
        current_sum += cardPoints[i]
        prefix.append(current_sum)
    
    suffix = [0]
    current_sum = 0
    for i in range(1, k + 1):
        current_sum += cardPoints[-i]
        suffix.append(current_sum)
    
    max_score = 0
    for l in range(0, k + 1):
        r = k - l
        current = prefix[l] + suffix[r]
        if current > max_score:
            max_score = cur