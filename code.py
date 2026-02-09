def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    n = int(data[idx])
    m = int(data[idx + 1])
    idx += 2
    for _ in range(m):
        ai = int(data[idx])
        bi = int(data[idx + 1])
        ci = int(data[idx + 2])
        idx += 3
        if ai == 1:
            print(0)
        elif bi == n:
            print(0)
        else:
            if ai < bi:
                print(0)
            else:
                print(1)

if __name__ == '__mai