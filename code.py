def maxSumTwoNoOverlap(A, L, M):
    n = len(A)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i+1] = prefix[i] + A[i]
    
    # Precompute max_m_after and max_l_after
    max_m_after = [0] * n
    for i in range(n - M, -1, -1):
        current = prefix[i + M] - prefix[i]
        if i == n - M:
            max_m_after[i] = current
        else:
            max_m_after[i] = max(current, max_m_after[i+1])
    
    max_l_after = [0] * n
    for i in range(n - L, -1, -1):
        