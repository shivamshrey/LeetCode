# 2251. Number of Flowers in Full Bloom
# https://leetcode.com/problems/number-of-flowers-in-full-bloom/

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        start_times = sorted(start for start, end in flowers)
        end_times = sorted(end for start, end in flowers)
        result = []
        
        for t in persons:
            upper_bound = bisect.bisect_right(start_times, t)    # num of flowers started blooming for time = t
            lower_bound = bisect.bisect_left(end_times, t)   # num of flowers stopped blooming for time = t
            result.append(upper_bound - lower_bound)
        
        return result