# 2200. Find All K-Distant Indices in an Array
# https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        result = list()
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[j] == key and abs(i - j) <= k:
                    result.append(i)
                    break
        
        return result