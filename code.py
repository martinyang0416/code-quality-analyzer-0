def maxRepOpt1(text):
    from collections import defaultdict

    # Split the text into groups of consecutive characters
    groups = []
    n = len(text)
    if n == 0:
        return 0
    current_char = text[0]
    start = 0
    for i in range(1, n):
        if text[i] != current_char:
            groups.append((current_char, start, i - 1))
            current_char = text[i]
            start = i
    groups.append((current_char, start, n - 1))

    # Organize groups by character
    char_gro