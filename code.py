def main():
    import sys
    n = int(sys.stdin.readline())
    adj = [[] for _ in range(n + 1)]
    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        adj[a].append(b)
        adj[b].append(a)
    
    # Check if each node has exactly two neighbors
    for i in range(1, n + 1):
        if len(adj[i]) != 2:
            print(-1)
            return
    
    sequence = [1]
    current = 1
    prev = -1  # Indicates no previous node at the start
    
    for _ in rang