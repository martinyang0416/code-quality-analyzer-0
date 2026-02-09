import sys

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    for _ in range(T):
        N, M = int(data[idx]), int(data[idx+1])
        idx +=2
        A = list(map(int, data[idx:idx+N]))
        idx +=N
        s = set(A)
        valid = True
        for x in range(1, M):
            if x not in s:
                valid = False
                break
        if not valid:
            print(-1)
            continue
        count