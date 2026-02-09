MOD = 10**9 + 7

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sub_sums = []
        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += nums[j]
                sub_sums.append(current_sum)
        sub_sums.sort()
        total = sum(sub_sums[left-1:right])
        return total % MOD