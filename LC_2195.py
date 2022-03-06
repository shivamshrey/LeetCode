# 2195. Append K Integers With Minimal Sum
# https://leetcode.com/problems/append-k-integers-with-minimal-sum/

class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        level = k + 1
        result = k * (k + 1) // 2   # multiply then divide
        
        for num in sorted(set(nums)):
            if num < level:
                result += level - num
                level += 1
        
        return result
        