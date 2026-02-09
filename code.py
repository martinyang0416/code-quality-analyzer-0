from typing import List

class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        def calculate(start):
            arr = nums.copy()
            moves = 0
            n = len(arr)
            for i in range(start, n, 2):
                current = nums[i]
                if i > 0:
                    required = current - 1
                    if arr[i-1] > required:
                        moves += arr[i-1] - required
                        arr[i-1] = required
          