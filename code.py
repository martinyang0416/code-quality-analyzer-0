class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        len_s, len_p = len(s), len(p)
        dp = [[False] * (len_p + 1) for _ in range(len_s + 1)]
        dp[len_s][len_p] = True
        
        for i in range(len_s, -1, -1):
            for j in range(len_p - 1, -1, -1):
                first_match = i < len_s and (p[j] == s[i] or p[j] == '.')
                if j + 1 < len_p and p[j + 1] == '*':
                    dp[i][j] = dp[i][j + 2] or (first_match and dp[i + 1][j])
   