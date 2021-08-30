# 506. Relative Ranks

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        maxheap = []
        for i, s in enumerate(score):
            maxheap.append([-s, i])
            
        heapq.heapify(maxheap)
        
        answer = [""] * len(score)
        
        place = 1
        while maxheap:
            i = heapq.heappop(maxheap)[1]
            
            if place == 1:
                answer[i] = "Gold Medal"
            elif place == 2:
                answer[i] = "Silver Medal"
            elif place == 3:
                answer[i] = "Bronze Medal"
            else:
                answer[i] = str(place)
            place += 1
        
        return answer
    