# 300. Longest Increasing Subsequence

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # tail[i] = minimum possible tail value of LIS of length (i + 1)
        tail = [nums[0]]
        
        for i in range(1, len(nums)):
            if nums[i] > tail[-1]:
                tail.append(nums[i])
            else:
                # find ceiling element of nums[i] using binary search
                # and replace it with nums[i]
                ceiling = bisect.bisect_left(tail, nums[i])
                tail[ceiling] = nums[i]
        
        return len(tail)
    