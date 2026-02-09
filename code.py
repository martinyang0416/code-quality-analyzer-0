import sys

def generate_all_pairings():
    numbers = [1, 2, 3, 4, 5, 6]
    all_p = []

    def helper(remaining, path):
        if not remaining:
            all_p.append(path)
            return
        first = remaining[0]
        for i in range(1, len(remaining)):
            pair = (first, remaining[i])
            new_remaining = remaining[1:i] + remaining[i+1:]
            helper(new_remaining, path + [pair])

    helper(numbers, [])
    return all_p

all_pairings = generate_all_pairing