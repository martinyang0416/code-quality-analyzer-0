import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    drinks = list(map(int, sys.stdin.readline().split()))
    guests = []
    for i in range(m):
        x, y = map(int, sys.stdin.readline().split())
        guests.append((x-1, y-1))  # Convert to 0-based indices

    # Track forced guests and their choices
    forced = [False] * m
    chosen = [None] * m
    remaining = drinks.copy()
    possible = True

    for idx in range(m):
        x, y = guests[idx]
        a_zero