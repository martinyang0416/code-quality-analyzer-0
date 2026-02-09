import sys

def generate_partitions(remaining):
    if not remaining:
        return [ [] ]
    first = remaining[0]
    res = []
    for i in range(1, len(remaining)):
        second = remaining[i]
        new_remaining = remaining[1:i] + remaining[i+1:]
        for p in generate_partitions(new_remaining):
            res.append( [ (first, second) ] + p )
    return res

# Precompute all possible partitions for 6 elements
all_partitions = generate_partitions([1,2,3,4,5,6])

def main():
    inpu