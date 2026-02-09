def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0

    t = input[idx]
    idx += 1
    N = len(t)
    U = int(input[idx])
    idx += 1
    updates = []
    for _ in range(U):
        p = int(input[idx]) - 1  # converting to 0-based
        c = input[idx + 1]
        updates.append((p, c))
        idx += 2

    target_sequence = ['b', 'e', 's', 's', 'i', 'e']
    def compute_contributions(s):
        completions = []
        current_s = 0
        current_state = 0
      