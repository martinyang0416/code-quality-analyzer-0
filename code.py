import bisect

class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        MOD = 10**9 + 7
        A.sort()
        n = len(A)
        count = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                required = target - A[i] - A[j]
                left = bisect.bisect_left(A, required, j + 1, n)
                right = bisect.bisect_right(A, required, j + 1, n)
                count += right - left
        return count % MOD