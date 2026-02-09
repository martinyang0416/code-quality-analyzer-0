import sys

def find_short_phrase_start(words):
    n = len(words)
    for start in range(n):
        # Check group 1: sum 5
        g1_sum = 0
        g1_end = start
        while g1_end < n:
            g1_sum += len(words[g1_end])
            if g1_sum == 5:
                break
            elif g1_sum > 5:
                g1_sum = -1
                break
            g1_end += 1
        if g1_sum != 5:
            continue
        
        # Check group 2: sum 7
        g2_start = g1_end + 