# 16. 3Sum Closest

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = sum(nums[:3])
        
        for i in range(len(nums) - 2):
            low = i + 1
            high = len(nums) - 1
            
            while low < high:
                cur_sum = nums[i] + nums[low] + nums[high]
                if abs(target - cur_sum) < abs(target - result):
                    result = cur_sum
                    
                if cur_sum < target:
                    low += 1
                elif cur_sum > target:
                    high -= 1
                else:
                    return result   # break early

        return result
    