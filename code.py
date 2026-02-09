import math
from typing import List

class Solution:
    def numSquarefulPerms(self, A: List[int]) -> int:
        A.sort()
        n = len(A)
        self.count = 0

        def is_perfect_square(s):
            root = math.isqrt(s)
            return root * root == s

        def backtrack(last, mask):
            if mask == (1 << n) - 1:
                self.count += 1
                return
            for i in range(n):
                if mask & (1 << i):
                    continue
      