def minCut(s):
    n = len(s)
    if n == 0:
        return 0
    # Precompute palindrome table
    is_pal = [[False] * n for _ in range(n)]
    for i in range(n-1, -1, -1):
        for j in range(i, n):
            if i == j:
                is_pal[i][j] = True
            elif j == i + 1:
                is_pal[i][j] = (s[i] == s[j])
            else:
                is_pal[i][j] = (s[i] == s[j] and is_pal[i+1][j-1])
    
    # Compute minimum cuts
    dp = [0] * n
    for i in range(n):
     