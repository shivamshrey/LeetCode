# 525. Contiguous Array
# https://leetcode.com/problems/contiguous-array/

# TC: O(n)
# SC: O(n)
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hashmap = {0: -1}
        count, result = 0, 0
        for i, num in enumerate(nums):
            count += 1 if num == 1 else -1
            result = max(result, i - hashmap.setdefault(count, i))
        return result
    