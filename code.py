import math

def readint():
    return list(map(int, input().split()))

def main():
    M, P = map(int, input().split())
    zones = []
    for _ in range(M):
        x, y, z, r, e = map(int, input().split())
        zones.append((x, y, z, r, e))
    
    for _ in range(P):
        sx, sy, sz, dx, dy, dz = map(int, input().split())
        A = (sx, sy, sz)
        B = (dx, dy, dz)
        total_e = 0
        
        for (cx, cy, cz, r, e) in zones:
            # Compute dA_sq and dB_sq
        