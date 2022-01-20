# 875. Koko Eating Bananas

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        
        while low < high:
            speed = (low + high) // 2
            hours = 0
            
            # Iterate over the piles and calculate hours.
            # We increase the hours by ceil(pile / speed)
            for pile in piles:
                hours += math.ceil(pile / speed)
            
            if hours <= h:
                high = speed
            else:
                low = speed + 1
        
        return high
    