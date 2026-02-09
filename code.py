def main():
    import sys

    fixed_A = "What are you doing while sending "  # length 34
    fixed_B = " Are you busy? Will you send "      # length 29
    f0 = "What are you doing at the end of the world? Are you busy? Will you save us?"  # length 75

    q = int(sys.stdin.readline())
    output = []

    for _ in range(q):
        n, k = map(int, sys.stdin.readline().split())
        current_n = n
        current_k = k
        ans = '.'  # default if out of bounds

        while current_n > 