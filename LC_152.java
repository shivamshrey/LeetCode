// 152. Maximum Product Subarray

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = nums[0]
        cur_min = nums[0]
        final_max = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                cur_max, cur_min = cur_min, cur_max
            cur_max = max(cur_max * nums[i], nums[i])
            cur_min = min(cur_min * nums[i], nums[i])
            final_max = max(cur_max, final_max)
        
        return final_max
