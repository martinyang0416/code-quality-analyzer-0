class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10**9 + 7
        transitions = [
            [4, 6],          # 0
            [6, 8],          # 1
            [7, 9],          # 2
            [4, 8],          # 3
            [0, 3, 9],       # 4
            [],               # 5
            [0, 1, 7],       # 6
            [2, 6],          # 7
            [1, 3],          # 8
            [2, 4]           # 9
        ]
        if n == 1:
            return 10
        pre