# 503. Next Greater Element II

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        result = [-1] * len(nums)
    
        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                result[stack.pop()] = nums[i]
            stack.append(i)
        
        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                result[stack.pop()] = nums[i]
            stack.append(i)
        
        return result
    