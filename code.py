n = int(input())
rectangles = []
events = []

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    # Convert to inclusive intervals
    y_low = min(y1, y2)
    y_high = max(y1, y2)
    # Add start and end events
    events.append((x1, 'start', y_low, y_high))
    events.append((x2, 'end', y_low, y_high))

# Sort events: first by x, then end events before start events
events.sort(key=lambda e: (e[0], e[1] == 'end'))

active_intervals = []
prev_x = None
total_area = 0

for event i