# 2256. Minimum Average Difference
# https://leetcode.com/problems/minimum-average-difference/

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = [nums[0]]
        for i in range(1, n):
            prefix_sum.append(nums[i] + prefix_sum[i - 1])
        
        diff = float('inf')
        index = 0
        for i in range(n):
            first = prefix_sum[i] // (i + 1)
            last = 0 if n - 1 - i == 0 else (prefix_sum[-1] - prefix_sum[i]) // (n - 1 - i)
            if abs(first - last) < diff:
                diff = abs(first - last)
                index = i
        
        return index
    