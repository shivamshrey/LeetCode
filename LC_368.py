# 368. Largest Divisible Subset
# https://leetcode.com/problems/largest-divisible-subset/

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        dp = [1] * n
        hm = [0] * n
        maxi = 1
        last_index = 0
        for i in range(n):
            hm[i] = i
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    hm[i] = j
            if dp[i] > maxi:
                maxi = dp[i]
                last_index = i

        temp = [nums[last_index]]
        while last_index != hm[last_index]:
            last_index = hm[last_index]
            temp.append(nums[last_index])

        return temp[::-1]
    