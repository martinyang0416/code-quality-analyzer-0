import bisect

def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    N = int(input[idx])
    idx += 1
    Q = int(input[idx])
    idx += 1

    s = input[idx]
    idx += 1

    L_indices = []
    R_indices = []
    for i, c in enumerate(s):
        if c == 'L':
            L_indices.append(i)
        else:
            R_indices.append(i)

    # Compute ℓ and r arrays (0-based)
    l = [L_indices[i] + 1 for i in range(N)]
    r = [R_indices[i] + 1 for i in range(N)]

   