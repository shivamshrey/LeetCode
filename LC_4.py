# 4. Median of Two Sorted Arrays

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        n1, n2 = len(nums1), len(nums2)
        
        begin = 0
        end = n1
        
        while begin <= end:
            i1 = int((begin + end) / 2)
            i2 = int((n1 + n2 + 1) / 2 - i1)
            
            min1 = sys.maxsize if i1 == n1 else nums1[i1]
            max1 = -sys.maxsize if i1 == 0 else nums1[i1 - 1]
            min2 = sys.maxsize if i2 == n2 else nums2[i2]
            max2 = -sys.maxsize if i2 == 0 else nums2[i2 - 1]
            
            if max1 <= min2 and max2 <= min1 :
                if (n1 + n2) % 2 == 0:
                    return ((max(max1, max2) + min(min1, min2)) / 2)
                else:
                    return max(max1, max2)
            elif max1 > min2:
                end = i1 - 1
            else:
                begin = i1 + 1
        