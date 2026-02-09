def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    t = input[idx]
    idx += 1
    U = int(input[idx])
    idx += 1
    updates = []
    for _ in range(U):
        p = int(input[idx]) - 1  # converting to 0-based
        c = input[idx+1]
        updates.append((p, c))
        idx += 2

    target = ['b', 'e', 's', 's', 'i', 'e']

    def compute_A(s):
        n = len(s)
        # Precompute for each position the state when starting there
        # We can store for ea