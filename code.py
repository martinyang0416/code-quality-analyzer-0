import bisect

def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    d = int(input[ptr])
    ptr +=1
    n = int(input[ptr])
    m = int(input[ptr+1])
    ptr +=2

    points = []
    for _ in range(d):
        x = int(input[ptr])
        y = int(input[ptr+1])
        points.append( (x, y) )
        ptr +=2

    cnt_left = int(input[ptr])
    cnt_right = int(input[ptr+1])
    cnt_top = int(input[ptr+2])
    cnt_bottom = int(input[ptr+3])
    ptr +=4

    # Create set of