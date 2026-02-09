import sys
import math

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    index = 1
    for _ in range(t):
        x = int(data[index])
        y = int(data[index + 1])
        index += 2
        g = math.gcd(x, y)
        lcm = x * y // g
        a = lcm // x
        b = lcm // y
        print(a + b - 2)

if __name__ == '__main__':
    main()