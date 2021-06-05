# 1512. Number of Good Pairs

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hm = dict()
        for num in nums:
            hm[num] = hm.get(num, 0) + 1
        
        count = 0
        for key, value in hm.items():
            count += value * (value - 1) // 2
        
        return count
    