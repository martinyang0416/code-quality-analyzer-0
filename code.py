from typing import List

class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        n = len(A)
        max_left = [0] * n
        max_left[0] = A[0]
        for i in range(1, n):
            max_left[i] = max(max_left[i-1], A[i])
        
        min_right = [0] * n
        min_right[-1] = A[-1]
        for i in range(n-2, -1, -1):
            min_right[i] = min(min_right[i+1], A[i])
        
        for i in range(n-1):
            if max_left[i] <= min_right[i+1]:
          