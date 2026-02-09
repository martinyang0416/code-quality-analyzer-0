x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
cx, cy = map(int, input().split())

def check():
    for t in range(4):
        if t == 0:
            rax, ray = x1, y1
        elif t == 1:
            rax, ray = y1, -x1
        elif t == 2:
            rax, ray = -x1, -y1
        else:
            rax, ray = -y1, x1
        
        dx = x2 - rax
        dy = y2 - ray
        
        if cx == 0 and cy == 0:
            if dx == 0 and dy == 0:
                return True
 