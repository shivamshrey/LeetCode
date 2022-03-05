# 740. Delete and Earn
# https://leetcode.com/problems/delete-and-earn/

# TC: O(N + k)
# SC: O(N)

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = collections.defaultdict(int)
        # points[num] = num * no. of occurrences of num in nums
        #             = points gained by taking all occurrences of num
        max_number = nums[0]
        for num in nums:
            points[num] += num
            max_number = max(max_number, num)
        
        two_back = 0
        one_back = points.get(1, 0)
        
        for num in range(2, max_number + 1):
            two_back, one_back = one_back, max(one_back, points.get(num, 0) + two_back)
        
        return one_back
        