def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    N = int(input[ptr])
    ptr += 1
    M = float(input[ptr])
    ptr += 1

    cylinders = []

    for _ in range(N):
        K = int(input[ptr])
        ptr += 1
        for i in range(K):
            S = float(input[ptr])
            ptr += 1
            H = float(input[ptr])
            ptr += 1
            cylinders.append((S, H))

    # Sort by base area (S)
    cylinders.sort(key=lambda x: x[0])

    total_height