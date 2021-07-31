# 57. Insert Interval

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        prev = newInterval
        
        for cur in intervals:
            # if current is completely past previous interval
            if prev[1] < cur[0]:
                result.append(prev)
                prev = cur
            # if current is completely before previous interval
            elif cur[1] < prev[0]:
                result.append(cur)
            # if there's an overlap
            else:
                prev[0] = min(prev[0], cur[0])
                prev[1] = max(prev[1], cur[1])
        
        result.append(prev)
        
        return result
