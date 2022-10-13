# 198. House Robber
# https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3: return max(nums)
        prev2 = nums[0]
        prev1 = max(nums[0], nums[1])
        for i in range(2, n):
            cur = max(nums[i] + prev2, prev1)
            prev2 = prev1
            prev1 = cur
        return prev1
    