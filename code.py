def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    L = int(input[idx])
    idx += 1
    for _ in range(L):
        M = int(input[idx])
        idx += 1
        P = int(input[idx])
        idx += 1
        n = M + P - 1
        k = P
        if k == 0:
            print(1 % 1000000000)
            continue
        result = 1
        for i in range(1, k + 1):
            result = result * (n - i + 1) // i
        print(result % 1000000000)

if __name__ == "__main__":
 