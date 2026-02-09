def main():
    import sys
    s = sys.stdin.readline().strip()
    n = len(s)
    if n == 0:
        print(0)
        return

    target = ['b', 'e', 's', 's', 'i', 'e']
    progress = [0] * 6
    count = 0
    cnt = [0] * n

    for i in range(n):
        c = s[i]
        for j in range(5, -1, -1):
            if j == 0:
                if c == target[0]:
                    progress[0] += 1
            else:
                if c == target[j] and progress[j-1] > 0:
                    progress