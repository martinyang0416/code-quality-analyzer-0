def maxDistToClosest(seats):
    occupied = [i for i, seat in enumerate(seats) if seat == 1]
    left = occupied[0]
    right = len(seats) - 1 - occupied[-1]
    max_dist = max(left, right)
    for i in range(1, len(occupied)):
        distance = (occupied[i] - occupied[i-1]) // 2
        if distance > max_dist:
            max_dist = distance
    return max_dist