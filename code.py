def checkInclusion(s1: str, s2: str) -> bool:
    n, m = len(s1), len(s2)
    if n > m:
        return False
    
    s1_counts = [0] * 26
    window_counts = [0] * 26
    
    for i in range(n):
        s1_counts[ord(s1[i]) - ord('a')] += 1
        window_counts[ord(s2[i]) - ord('a')] += 1
    
    if s1_counts == window_counts:
        return True
    
    for i in range(n, m):
        outgoing = s2[i - n]
        window_counts[ord(outgoing) - ord('a')] -= 1
        incoming = s2[i]
        wi