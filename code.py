import sys

def main():
    input = sys.stdin.read().split()
    T = int(input[0])
    index = 1
    for _ in range(T):
        R = int(input[index])
        C = int(input[index+1])
        G = int(input[index+2])
        index +=3
        remaining = G
        current_col = C
        previous = None
        steps = []
        while remaining > 0 and current_col >= 0:
            w = current_col
            if steps:
                max_allowed = previous
            else:
                max_al