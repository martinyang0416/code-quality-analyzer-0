def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    for _ in range(T):
        N = int(input[idx])
        idx += 1
        K = input[idx].strip()
        idx += 1
        mod = 0
        for c in K:
            mod = (mod * 10 + int(c)) % N
        if mod == 0:
            print(0)
        else:
            print(2 * min(mod, N - mod))

if __name__ == "__main__":
    main()