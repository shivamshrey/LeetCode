# 2419. Longest Subarray With Maximum Bitwise AND
# https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/

# TC: O(n)
# SC: O(1)

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_num = max(nums)
        result = length = 0
        for num in nums:
            if num == max_num: 
                length += 1
                result = max(result, length)
            else: 
                length = 0
            
        return result