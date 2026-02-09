n = int(input())
x = int(input())

m = n % 6

# Define the inverse permutations for each m (0 to 5)
inverse_perms = [
    [0, 1, 2],   # m=0
    [2, 1, 0],   # m=1
    [1, 2, 0],   # m=2
    [0, 2, 1],   # m=3
    [2, 0, 1],   # m=4
    [1, 0, 2]    # m=5
]

# Get the inverse permutation for m steps
inv_perm = inverse_perms[m]

# The initial position is inv_perm[x]
print(inv_perm[x])