# 57. Insert Interval

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        new_start = newInterval[0]
        new_end = newInterval[1]
        
        for interval in intervals:
            cur_start = interval[0]
            cur_end = interval[1]
            # if current is completely before newInterval
            if cur_end < new_start:
                result.append(interval)
            # if newInterval is completely past current
            elif new_end < cur_start:
                result.append([new_start, new_end])
                # make current as newInterval
                new_start = cur_start
                new_end = cur_end
            # if there's an overlap
            else:
                new_start = min(cur_start, new_start)
                new_end = max(cur_end, new_end)
        
        result.append([new_start, new_end])
        
        return result
