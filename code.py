class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row, cols, diag1, diag2):
            if row == n:
                return 1
            count = 0
            for col in range(n):
                d1 = row - col
                d2 = row + col
                if col not in cols and d1 not in diag1 and d2 not in diag2:
                    cols.add(col)
                    diag1.add(d1)
                    diag2.add(d2)
                    count += backtrack(row + 1, 