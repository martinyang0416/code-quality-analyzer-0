import math
import heapq

def generate_edges(star):
    x, y, a_deg, r = star
    tips = []
    for k in range(5):
        angle_deg = a_deg + 72 * k
        angle_rad = math.radians(angle_deg)
        tip_x = x + r * math.sin(angle_rad)
        tip_y = y + r * math.cos(angle_rad)
        tips.append((tip_x, tip_y))
    edges = [
        (tips[0], tips[2]),
        (tips[2], tips[4]),
        (tips[4], tips[1]),
        (tips[1], tips[3]),
        (tips[3], tips[0])
    ]
    return edges

def c