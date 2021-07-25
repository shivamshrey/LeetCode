# 1423. Maximum Points You Can Obtain from Cards

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        window_size = len(cardPoints) - k
        total_sum = cur_sum = min_sum = sum(cardPoints[:window_size])
        
        for i in range(window_size, len(cardPoints)):
            cur_sum += cardPoints[i] - cardPoints[i - window_size]
            min_sum = min(min_sum, cur_sum)
            total_sum += cardPoints[i]
            
        return total_sum - min_sum
    