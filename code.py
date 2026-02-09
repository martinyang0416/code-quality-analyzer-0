import bisect

def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    N = int(input[idx])
    idx +=1
    Q = int(input[idx])
    idx +=1

    S = input[idx]
    idx +=1
    special_str = input[idx]
    idx +=1

    # Parse the left and right endpoints
    left = []
    for i in range(N):
        if S[i] == 'L':
            left.append(i)
    right = []
    for i in range(N, 2*N):
        if S[i] == 'R':
            right.append(i - N)

    # Precompute farthest array
  