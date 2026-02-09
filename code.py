import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    ptr = 0
    N, Q = data[ptr], data[ptr+1]
    ptr += 2
    A = data[ptr:ptr+N]
    ptr += N
    queries = data[ptr:ptr+Q]
    s = set(A)
    for x in queries:
        print("YES" if x in s else "NO")

if __name__ == "__main__":
    main()