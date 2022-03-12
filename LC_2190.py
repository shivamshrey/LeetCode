# 2190. Most Frequent Number Following Key In an Array
# https://leetcode.com/problems/most-frequent-number-following-key-in-an-array/

# TC: O(n)
# SC: O(no. of occurrence of key in nums)
class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        targets = defaultdict(int) # frequency of all potential targets
        result = 0
        for i in range(len(nums) - 1):
            if nums[i] == key:   
                targets[nums[i + 1]] += 1
                if targets[nums[i + 1]] > targets[result]:
                    result = nums[i + 1]
        return result
    