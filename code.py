import numpy as np

n = int(input())
a = list(map(int, input().split()))

if n == 1:
    exit()

bits = [0] * (n - 1)
for d in range(1, n):
    bits[d-1] = bin(d).count('1')

a_np = np.array(a, dtype=np.float64)
bits_np = np.array(bits, dtype=np.float64)

size = 1
while size < len(a_np) + len(bits_np) - 1:
    size <<= 1

fft_a = np.fft.fft(a_np, size)
fft_bits = np.fft.fft(bits_np, size)

fft_conv = fft_a * fft_bits
conv = np.fft.ifft(fft_conv).real

result = []
for k in range(1, n):
    index 