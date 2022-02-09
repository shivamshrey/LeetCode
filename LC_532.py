# 532. K-diff Pairs in an Array
# https://leetcode.com/problems/k-diff-pairs-in-an-array/

# TC: O(n)
# SC: O(n)
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        result = 0
        counts = collections.Counter(nums)
        
        for num in counts:
            if k > 0 and num + k in counts or k == 0 and counts[num] > 1:
                result += 1
        return result
    
