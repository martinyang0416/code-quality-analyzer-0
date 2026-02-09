def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    for _ in range(T):
        N = int(input[idx])
        K = int(input[idx + 1])
        idx += 2
        if K > 81:
            print(-1)
            continue
        index = K - 1
        a = (index // 9) + 1
        idx_in_group = index % 9
        sorted_b = []
        if 0 != a:
            sorted_b.append(0)
        for x in range(1, 10):
            if x != a:
               