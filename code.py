def generate_all_pairings():
    nums = [1, 2, 3, 4, 5, 6]
    all_pairings = []

    def backtrack(remaining, current):
        if not remaining:
            all_pairings.append(current.copy())
            return
        first = remaining[0]
        for i in range(1, len(remaining)):
            pair = (first, remaining[i])
            new_remaining = remaining[1:i] + remaining[i+1:]
            current.append(pair)
            backtrack(new_remaining, current)
            current.pop()

    ba