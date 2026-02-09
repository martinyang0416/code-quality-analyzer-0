import sys

MOD = 10**9 + 7

def main():
    data = sys.stdin.read().split()
    ptr = 0
    T = int(data[ptr])
    ptr += 1
    results = []
    for _ in range(T):
        d = int(data[ptr])
        ptr += 1
        L = int(data[ptr])
        R = int(data[ptr+1])
        ptr += 2
        
        # Calculate start_odd and end_odd
        start_odd = L if L % 2 == 1 else L + 1
        end_odd = R if R % 2 == 1 else R - 1
        
        # Compute N
        N = ((end_odd - start_odd) // 2) + 1
 