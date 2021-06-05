# 1512. Number of Good Pairs

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hm = dict()
        count = 0
        for num in nums:
            count += hm.get(num, 0)
            hm[num] = hm.get(num, 0) + 1
        
        return count
    