# 2202. Maximize the Topmost Element After K Moves
# https://leetcode.com/problems/maximize-the-topmost-element-after-k-moves/

class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 1:
            return -1 if k % 2 == 1 else nums[0]
        
        max_number = 0
        for i in range(n):
            if i == k or i + 2 <= k:
                max_number = max(max_number, nums[i])
        
        return max_number
        