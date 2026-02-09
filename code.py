class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1_sorted = sorted(s1)
        s2_sorted = sorted(s2)
        condition1 = all(c1 >= c2 for c1, c2 in zip(s1_sorted, s2_sorted))
        condition2 = all(c2 >= c1 for c1, c2 in zip(s1_sorted, s2_sorted))
        return condition1 or condition2