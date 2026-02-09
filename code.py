import sys
from collections import defaultdict

def main():
    E_M = sys.stdin.readline().split()
    while len(E_M) < 2:
        line = sys.stdin.readline()
        if not line:
            break
        E_M += line.split()
    E = int(E_M[0])
    M = int(E_M[1])

    emoticons = []
    for _ in range(E):
        line = sys.stdin.readline().strip()
        while not line:
            line = sys.stdin.readline().strip()
        emoticons.append(line)

    # Build prefix map
    prefix_map = def