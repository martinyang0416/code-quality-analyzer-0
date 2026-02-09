def longestStrChain(words):
    words = list(set(words))  # Remove duplicates
    words.sort(key=lambda x: len(x))  # Sort by length
    from collections import defaultdict

    def is_predecessor(s, t):
        if len(t) != len(s) + 1:
            return False
        for i in range(len(t)):
            if t[:i] + t[i+1:] == s:
                return True
        return False

    dp = defaultdict(int)
    max_chain = 0
    length_groups = defaultdict(list)
    for word in words:
        length