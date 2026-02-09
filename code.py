a = int(input())
binary = bin(a)[2:].zfill(6)
bits = list(map(int, binary))
output_bits = [bits[0], bits[5], bits[3], bits[2], bits[4], bits[1]]
result = int(''.join(map(str, output_bits)), 2)
print(result)