# 496. Next Greater Element I

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hm = dict()
        stack = []
        result = []
        
        for num in nums2:
            while stack and num > stack[-1]:
                hm[stack.pop()] = num
            stack.append(num)
        
        for num in nums1:
            result.append(hm.get(num, -1))
        
        return result
    