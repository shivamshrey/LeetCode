# 630. Course Schedule III
# https://leetcode.com/problems/course-schedule-iii/

# TC: O (n log n)
# SC: O (n)
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda item: item[1])  # early deadlines first
        
        maxheap = []
        time = 0
        for duration, last_day in courses:
            time += duration
            heapq.heappush(maxheap, -duration)
            if time > last_day:
                time -= -heapq.heappop(maxheap)
        return len(maxheap)
