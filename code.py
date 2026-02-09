MOD = 10**9 + 7

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        max_pos = min(arrLen - 1, steps)
        prev = [0] * (max_pos + 1)
        prev[0] = 1
        
        for _ in range(steps):
            current = [0] * (max_pos + 1)
            for j in range(max_pos + 1):
                current[j] = prev[j]
                if j > 0:
                    current[j] += prev[j - 1]
                if j < max_pos:
                    current[j] += prev[j + 1]
      