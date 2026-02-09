MOD = 10**9 + 7

class Solution:
    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        n = len(group)
        # Initialize DP table. dp[j][k] represents the number of schemes using j members and at least k profit (capped at P)
        dp = [[0] * (P + 1) for _ in range(G + 1)]
        dp[0][0] = 1  # Base case: 0 members, 0 profit, 1 way
        
        for i in range(n):
            current_g = group[i]
            current_p = profit[i]
          