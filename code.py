def main():
    s = input().strip()
    n = len(s)
    if n == 0:
        print(0)
        return

    # Define direction deltas: north, east, south, west
    direction_deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # Precompute suffix dx, dy, and final direction for each position and starting direction
    suffix_dx = [[0]*4 for _ in range(n+1)]
    suffix_dy = [[0]*4 for _ in range(n+1)]
    suffix_dir = [[0]*4 for _ in range(n+1)]

    # Initialize for i = n (no commands)
    for d in range