# 2420. Find All Good Indices
# https://leetcode.com/problems/find-all-good-indices/

class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        prefix = [1] * (len(nums) + 1)    # non-increasing
        suffix = [1] * (len(nums) + 1)    # non-decreasing
        
        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]: prefix[i] = prefix[i - 1] + 1
         
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] <= nums[i + 1]: suffix[i] = suffix[i + 1] + 1
        
        return [i for i in range(k, len(nums) - k) if prefix[i - 1] >= k and suffix[i + 1] >= k]
    