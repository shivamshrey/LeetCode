# 740. Delete and Earn
# https://leetcode.com/problems/delete-and-earn/

# TC: O(N + k)
# SC: O(N + k)

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = collections.defaultdict(int)
        # points[num] = num * no. of occurrences of num in nums
        #             = points gained by taking all occurrences of num
        max_number = nums[0]
        for num in nums:
            points[num] += num
            max_number = max(max_number, num)
        
        maxPoints = [0] * (max_number + 1)
        # maxPoints[num] = max points that can be gained considering nums 0...num
        maxPoints[1] = points[1]
        
        for num in range(2, max_number + 1):
            maxPoints[num] = max(maxPoints[num - 2] + points[num],  # pick num
                                 maxPoints[num - 1])                # don't pick num
        
        return maxPoints[max_number]
        