def count_double_concatenations(text):
    s = set()
    n = len(text)
    for L in range(2, n + 1, 2):
        m = L // 2
        for i in range(n - L + 1):
            if text[i:i+m] == text[i+m:i+L]:
                s.add(text[i:i+L])
    return len(s)