from collections import Counter

def minSteps(s: str, t: str) -> int:
    count_s = Counter(s)
    count_t = Counter(t)
    steps = 0
    for c in 'abcdefghijklmnopqrstuvwxyz':
        steps += max(0, count_s[c] - count_t[c])
    return steps