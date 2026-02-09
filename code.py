import sys
from collections import defaultdict

MOD = 10**9 + 7

def main():
    n = int(sys.stdin.readline())
    actions = []
    place_x_counts = defaultdict(int)

    # Read all actions and track place occurrences
    for _ in range(n):
        parts = sys.stdin.readline().split()
        if parts[0] == "CLAIM":
            x = int(parts[1])
            actions.append(("CLAIM", x))
        else:
            x = int(parts[1])
            actions.append(("PLACE", x))
            place_x_counts