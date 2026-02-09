import sys

def main():
    lines = [line.strip() for line in sys.stdin if line.strip()]
    ptr = 0
    n, m, k = map(int, lines[ptr].split())
    ptr += 1
    
    sections = []
    for _ in range(6):
        section = []
        cnt = m if _ < 2 else n if _ < 4 else n
        for __ in range(cnt):
            section.append(list(map(int, lines[ptr].split())))
            ptr += 1
        sections.append(section)
    
    grid = [[[0]*k for _ in range(m)] for __ in range(n)]
    
    def proce