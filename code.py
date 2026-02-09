def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    N = int(input())
    F = int(input())
    f = list(map(int, input().split()))
    p = list(map(int, input().split()))

    def is_perfect_cube(x):
        if x < 1:
            return False
        n = 1
        while n ** 3 <= x:
            if n ** 3 == x:
                return True
            n += 1
        return False

    valid_f = []
    valid_p = []
    for i in range(N):
        fi = f[i]
        if not is_perfect_cube(