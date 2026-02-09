import sys
sys.setrecursionlimit(1 << 25)
MOD = 10**9 + 7

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    N = int(data[idx])
    idx +=1
    M = int(data[idx])
    idx +=1

    edges = []
    for _ in range(M):
        u = int(data[idx])
        idx +=1
        v = int(data[idx])
        idx +=1
        c = int(data[idx])
        idx +=1
        edges.append( (c, u-1, v-1) )

    # Sort edges by cost
    edges.sort()
    
    # Group edges by cos