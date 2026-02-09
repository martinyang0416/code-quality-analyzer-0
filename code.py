# Read the input values
M, N, P = map(int, input().split())

# Calculate the maximum hours based on money
hours_money = N // M

# The result is the minimum of the two limits
result = min(hours_money, P)

# Output the result
print(result)