from collections import deque

def racecar(target):
    queue = deque([(0, 1, 0)])
    visited = set([(0, 1)])
    
    while queue:
        pos, speed, steps = queue.popleft()
        
        if pos == target:
            return steps
        
        # Action A: Accelerate
        new_pos = pos + speed
        new_speed = speed * 2
        if (new_pos, new_speed) not in visited:
            # Prune positions that are too far from the target
            if abs(new_pos) <= 2 * target:
         