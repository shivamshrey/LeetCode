# 1550. Three Consecutive Odds

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0
        i = 0
        
        while i < len(arr) and count < 3:
            count = count + 1 if arr[i] & 1 else 0
            i += 1
        
        return count == 3
    