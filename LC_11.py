# 11. Container With Most Water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        low = 0
        high = len(height) - 1
        max_storage = 0

        while low < high:
            if height[low] < height[high]:
                max_storage = max(max_storage, (high - low) * height[low])
                low += 1
            elif height[low] > height[high]:
                max_storage = max(max_storage, (high - low) * height[high])
                high -= 1
            else:
                max_storage = max(max_storage, (high - low) * height[low])
                low += 1
                high -= 1

        return max_storage
