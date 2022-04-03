# 2226. Maximum Candies Allocated to K Children
# https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
        low, high = 1, sum(candies) // k
        
        while low != high:
            mid = (low + high + 1) >> 1
            
            if sum(i//mid for i in candies) >= k:
                low = mid
            else:
                high = mid-1
        return low
    