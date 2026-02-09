import sys

def check_triple(x, y, z):
    return not (x <= y <= z or x >= y >= z)

def is_valid_quadruple(a, b, c, d):
    return (check_triple(a, b, c) and check_triple(a, b, d) and
            check_triple(a, c, d) and check_triple(b, c, d))

def main():
    input = sys.stdin.read().split()
    ptr = 0
    n, q = int(input[ptr]), int(input[ptr+1])
    ptr +=2
    a = list(map(int, input[ptr:ptr+n]))
    ptr +=n
    for _ in range(q):
        L = int(input[ptr])-1
        R = int(input[ptr+1])