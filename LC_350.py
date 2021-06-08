# Intersection of Two Arrays II

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # for 2nd follow up question
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)
        result = []
        hm = dict()
        
        for num in nums1:
            hm[num] = hm.get(num, 0) + 1
        
        for num in nums2:
            if num in hm and hm[num] > 0:
                result.append(num)
                hm[num] -= 1
        
        return result
    