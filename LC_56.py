# 56. Merge Intervals

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if intervals == None or len(intervals) == 0:
            return []
        intervals.sort()
        result = [intervals[0]]
        
        for i in range(len(intervals)):
            if result[-1][1] >= intervals[i][0]:
                result[-1][1] = max(result[-1][1], intervals[i][1])
            else:
                result.append(intervals[i])
    
        return result
