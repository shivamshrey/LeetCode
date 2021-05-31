# 605. Can Place Flowers

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        count = 0
        while i < len(flowerbed) and count < n:
            if flowerbed[i] == 0:
                prev = flowerbed[i - 1] if i > 0 else 0
                next = flowerbed[i + 1] if i < len(flowerbed) - 1 else 0
                if prev == 0 and next == 0:
                    flowerbed[i] = 1
                    count += 1
                    i += 1
            i += 1
        
        return count == n
