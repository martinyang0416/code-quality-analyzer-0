def build_transition(pattern):
    len_p = len(pattern)
    failure = [0] * len_p
    for i in range(1, len_p):
        j = failure[i-1]
        while j > 0 and pattern[i] != pattern[j]:
            j = failure[j-1]
        if pattern[i] == pattern[j]:
            j += 1
        failure[i] = j
    transition = [[0]*26 for _ in range(len_p + 1)]
    for state in range(len_p + 1):
        for c in range(26):
            char = chr(ord('a') + c)
            j = state
            while True:
       