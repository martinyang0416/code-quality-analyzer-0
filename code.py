def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0

    target = "bessie"
    L = len(target)
    s = list(input[idx])
    idx += 1
    U = int(input[idx])
    idx += 1

    updates = []
    for _ in range(U):
        p = int(input[idx])
        c = input[idx+1]
        updates.append((p-1, c))  # convert to 0-based
        idx += 2

    def compute(s):
        n = len(s)
        previous_count = [0] * (L + 1)
        total = 0
        for i in range(n):
            curr