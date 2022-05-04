# 1679. Max Number of K-Sum Pairs
# https://leetcode.com/problems/max-number-of-k-sum-pairs/

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0
        low, high = 0, len(nums) - 1
        while low < high:
            if nums[low] + nums[high] < k:
                low += 1
            elif nums[low] + nums[high] > k:
                high -= 1
            else:
                low += 1
                high -= 1
                count += 1
        return count
    