def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def solve(array):
    lcm = (array[0] * array[1])//gcd(array[0], array[1])
    current = lcm
    for i in range(2, len(array)):
        running = (current * array[i])//gcd(current, array[i])
        lcm = gcd(lcm, running)
        current = gcd(current, array[i])
    print(lcm)
    return

n = int(input())
arr = list(map(int, input().split(' ')))
solve(arr)
