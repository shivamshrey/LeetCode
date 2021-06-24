# 15. 3Sum

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        
        for i in range(len(nums) - 2):
            if i == 0 or nums[i] != nums[i - 1]:
                low = i + 1
                high = len(nums) - 1
                target = 0 - nums[i]
                
                while low < high:
                    if nums[low] + nums[high] == target:
                        result.append([nums[i], nums[low], nums[high]])
                        # get to the last occurence of duplicate
                        # from low side
                        while low < high and nums[low] == nums[low + 1]:
                            low += 1
                        # and skip it
                        low += 1
                        # get to the last occurence of duplicate
                        # from high side
                        while low < high and nums[high] == nums[high - 1]:
                            high -= 1
                        # and skip it
                        high -= 1
                    elif nums[low] + nums[high] < target:
                        while low < high and nums[low] == nums[low + 1]:
                            low += 1
                        low += 1
                    else:
                        while low < high and nums[high] == nums[high - 1]:
                            high -= 1
                        high -= 1
        return result
    