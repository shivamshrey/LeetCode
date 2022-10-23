# 645. Set Mismatch
# https://leetcode.com/problems/set-mismatch/

# TC: O(n)
# SC: O(1)

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        duplicate, missing = -1, 1
        for num in nums:
            if nums[abs(num) - 1] < 0:
                duplicate = abs(num)
            else:
                nums[abs(num) - 1] *= -1
        
        for i in range(1, len(nums)):
            if nums[i] > 0:
                missing = i + 1
                break
        return [duplicate, missing]
    