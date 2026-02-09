fixed_part1 = "What are you doing while sending "  # 33 characters
fixed_part2 = " Are you busy? Will you send "     # 29 characters
f0_str = "What are you doing at the end of the world? Are you busy? Will you save us?"  # length 75

def solve():
    import sys
    input = sys.stdin.read().split()
    q = int(input[0])
    idx = 1
    res = []
    for _ in range(q):
        n = int(input[idx])
        k = int(input[idx+1])
        idx +=2
        
        def get_char(n, k):
            if n ==0