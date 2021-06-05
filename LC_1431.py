# 1431. Kids With the Greatest Number of Candies

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = [False] * len(candies)
        initial_max = max(candies)
        
        for i in range(len(candies)):
            result[i] = candies[i] + extraCandies >= initial_max
        
        return result
        