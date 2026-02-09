def solve(a):
    binary = bin(a)[2:].zfill(6)
    bits = list(binary)
    # The permutation indices are [0,5,3,2,4,1]
    new_bits = [bits[0], bits[5], bits[3], bits[2], bits[4], bits[1]]
    new_binary = ''.join(new_bits)
    return int(new_binary, 2)

a = int(input())
print(solve(a))