def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    n = int(input[idx]); idx +=1
    m = int(input[idx]); idx +=1
    k = int(input[idx]); idx +=1

    vertical_cuts = set()
    horizontal_cuts = set()

    for _ in range(k):
        x1 = int(input[idx]); y1 = int(input[idx+1]); x2 = int(input[idx+2]); y2 = int(input[idx+3])
        idx +=4
        if x1 == x2:
            vertical_cuts.add(x1)
        else:
            horizontal_cuts.add(y1)

    def compute_interva