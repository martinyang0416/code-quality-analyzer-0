import sys

def count_set_bits(n):
    return bin(n).count('1')

def main():
    input = sys.stdin.read
    data = input().split()
    T = int(data[0])
    for i in range(1, T+1):
        D = int(data[i])
        print(count_set_bits(D) - 1)

if __name__ == "__main__":
    main()