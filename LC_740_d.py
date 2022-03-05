# 740. Delete and Earn
# https://leetcode.com/problems/delete-and-earn/

# TC: O(N + K)
# SC: O(N)

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        prev_max, cur_max = 0, 0
        
        for num in range(max(counts.keys()) + 1):
            points = num * counts[num]
            prev_max, cur_max = cur_max, max(cur_max, points + prev_max)
        
        return cur_max
        