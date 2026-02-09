import math

def main():
    n = int(input())
    points = []
    for _ in range(n):
        x, y = map(float, input().split())
        points.append((x, y))
    
    sum_x = sum(x for x, y in points)
    sum_y = sum(y for x, y in points)
    sum_xy = sum(x * y for x, y in points)
    sum_x2 = sum(x**2 for x, y in points)
    
    numerator = n * sum_xy - sum_x * sum_y
    denominator = n * sum_x2 - sum_x ** 2
    
    if denominator == 0:
        theta_deg = 90.0
    else:
        m = numerator