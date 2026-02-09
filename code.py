# Read the input string
S = input().strip()

# Define the mirror mappings
mirror = {'b': 'd', 'd': 'b', 'p': 'q', 'q': 'p'}

# Reverse the string and replace each character with its mirror
reversed_S = S[::-1]
transformed = ''.join([mirror[c] for c in reversed_S])

# Check if the transformed string equals the original
print("Yes" if transformed == S else "No")