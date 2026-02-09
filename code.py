def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    n = int(input[idx])
    idx += 1
    m = int(input[idx])
    idx += 1
    d = int(input[idx])
    idx += 1
    D = d - n
    if D < 0:
        print(0)
        return

    planets = []
    for _ in range(n):
        ki = int(input[idx])
        idx += 1
        ci = int(input[idx])
        idx += 1
        planets.append((ki, ci))
    
    def f(x):
        total = 0
        for ki, ci in planets:
            denomin