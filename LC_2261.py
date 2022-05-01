# 2261. K Divisible Elements Subarrays
# https://leetcode.com/problems/k-divisible-elements-subarrays/

class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        seen = set()
        for i in range(len(nums)):
            temp, count = [], 0
            for j in range(i, len(nums)):
                temp.append(str(nums[j]))
                count += 0 if nums[j] % p else 1
                if count <= k:
                    seen.add('-'.join(temp))
        return len(seen)
            