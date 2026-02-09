M = int(input())
N = int(input())
mat = []
for _ in range(M):
    row = list(map(int, input().split()))
    mat.append(row)

# Transpose the matrix
transposed = list(zip(*mat))

# Reverse the order of the rows
rotated = transposed[::-1]

# Print the result
for row in rotated:
    print(' '.join(map(str, row)))