import sys

def main():
    input = sys.stdin.read().split()
    T = int(input[0])
    for i in range(1, T+1):
        N = int(input[i])
        print(N * (N + 3) // 2)

if __name__ == "__main__":
    main()