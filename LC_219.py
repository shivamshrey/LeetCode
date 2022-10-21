# 219. Contains Duplicate II
# https://leetcode.com/problems/contains-duplicate-ii/

# TC: O(n)
# SC: O(min(n, k))
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen: return True
            seen.add(nums[i])
            if len(seen) > k:
                seen.remove(nums[i - k])
        return False
    