import sys

def compute_inversion(arr):
    max_val = max(arr) if arr else 0
    n = len(arr)
    fenwick = [0] * (max_val + 2)
    inv_count = 0
    for i in reversed(range(n)):
        x = arr[i]
        # Query
        idx = x - 1
        while idx > 0:
            inv_count += fenwick[idx]
            idx -= idx & -idx
        # Update
        idx = x
        while idx <= max_val:
            fenwick[idx] += 1
            idx += idx & -idx
    return inv_count

def main():
    input = sys.st