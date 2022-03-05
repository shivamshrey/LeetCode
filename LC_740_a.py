# 740. Delete and Earn
# https://leetcode.com/problems/delete-and-earn/

# TC: O(N + k)
# SC: O(N + k)

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = collections.defaultdict(int)
        max_number = nums[0]
        for num in nums:
            points[num] += num
            max_number = max(max_number, num)
        
        @functools.cache
        def maxPoints(num):
            if num == 0:
                return 0
            if num == 1:
                return points[1]
            
            return max(maxPoints(num - 1),              # not picking num
                       points[num] + maxPoints(num - 2))    # picking num
        
        return maxPoints(max_number)
        