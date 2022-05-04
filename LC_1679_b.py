# 1679. Max Number of K-Sum Pairs
# https://leetcode.com/problems/max-number-of-k-sum-pairs/

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counts = dict()
        result = 0
        
        for num in nums:
            if counts.get(k - num, 0) > 0:
                counts[k - num] -= 1
                result += 1
            else:
                counts[num] = counts.get(num, 0) + 1
        
        return result
        