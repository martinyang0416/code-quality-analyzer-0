import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    # Read m edges (not used in the solution)
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
    t = list(map(int, sys.stdin.readline().split()))
    
    # Check if all topics are unique and cover 1..n
    topic_set = set()
    for num in t:
        if num < 1 or num > n:
            print(-1)
            return
        if num in topic_set:
            print(-1)
            return
        top