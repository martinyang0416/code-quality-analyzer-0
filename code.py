def main():
    import sys
    N, M = map(int, sys.stdin.readline().split())
    bits = bin(N).count('1')
    if M >= bits and (M - bits) % 2 == 0:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()