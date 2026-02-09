class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        N = len(A)
        diff = [0] * (N + 1)
        current_flips = 0
        flip_count = 0
        
        for i in range(N):
            current_flips += diff[i]
            actual = A[i] ^ (current_flips % 2)
            
            if actual == 0:
                if i + K > N:
                    return -1
                flip_count += 1
                current_flips += 1
                if i + K < N:
           