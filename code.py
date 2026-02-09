import sys

def main():
    input = sys.stdin.read
    data = input().split()
    T = int(data[0])
    index = 1
    for _ in range(T):
        P1 = int(data[index])
        P2 = int(data[index+1])
        K = int(data[index+2])
        index +=3
        total = P1 + P2
        quo = total // K
        print("CHEF" if quo % 2 == 0 else "COOK")

if __name__ == "__main__":
    main()