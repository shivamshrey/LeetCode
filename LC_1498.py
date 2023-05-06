# 1498. Number of Subsequences That Satisfy the Given Sum Condition
# TC: O(n⋅log⁡n)

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 1_000_000_007
        nums.sort()
        result = 0
        for i in range(len(nums)):
            j = bisect.bisect_right(nums, target - nums[i]) - 1
            if j >= i: result += pow(2, j - i, MOD)
        
        return result % MOD
