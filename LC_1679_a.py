# 1679. Max Number of K-Sum Pairs
# https://leetcode.com/problems/max-number-of-k-sum-pairs/

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counts = collections.Counter(nums)
        result = 0
        
        for num in nums:
            if counts.get(num, 0) > 0 and counts.get(k - num, 0) > 0:
                if num == k - num and counts.get(num) < 2: continue
                counts[num] -= 1
                counts[k - num] -= 1
                result += 1
        
        return result
        