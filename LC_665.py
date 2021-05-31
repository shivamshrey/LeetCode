# 665. Non-decreasing Array

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                count += 1
                # if previous to previous element is
                # also greater than current element,
                # then we have two choices:
                # 1. demote previous 2 elements
                # 2. promote current element
                # so we promote the current
                # element as it is only one modification
                if i - 2 >= 0 and nums[i - 2] > nums[i]:
                    nums[i] = nums[i - 1]
                # otherwise, we demote the previous element
                else:
                    nums[i - 1] = nums[i]
        
        return count <= 1
    