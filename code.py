import sys

def generate_pairings(elements):
    if not elements:
        return [ [] ]
    first = elements[0]
    result = []
    for i in range(1, len(elements)):
        pair = (first, elements[i])
        remaining = elements[1:i] + elements[i+1:]
        for sub in generate_pairings(remaining):
            result.append([pair] + sub)
    return result

# Precompute all possible pairings of 1-6
all_pairings = generate_pairings(list(range(1,7)))

def main():
    T = int(sys.stdin.readline())