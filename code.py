def main():
    import sys
    input = sys.stdin.read().split()
    t = int(input[0])
    cases = input[1:t+1]
    
    for s in cases:
        left = 0
        a = 0
        b = 0
        c = 0
        min_len = float('inf')
        for right in range(len(s)):
            char = s[right]
            if char == 'a':
                a += 1
            elif char == 'b':
                b += 1
            else:
                c += 1
            
            # Check if current window contains all t