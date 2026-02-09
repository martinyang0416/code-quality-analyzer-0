def longestPrefix(s: str) -> str:
    n = len(s)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i-1]
        while j > 0 and s[i] != s[j]:
            j = pi[j-1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    max_len = pi[-1]
    return s[:max_len] if max_len > 0 else ""