def main():
    import sys
    s = sys.stdin.read().strip()
    target = ['b', 'e', 's', 's', 'i', 'e']
    n = len(s)
    current_pos = 0
    start = -1
    events = []

    for i, c in enumerate(s):
        if current_pos == 0:
            if c == 'b':
                start = i
                current_pos = 1
            else:
                continue
        else:
            if c == target[current_pos]:
                current_pos += 1
                if current_pos == 6:
                   