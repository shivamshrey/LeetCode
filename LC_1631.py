# 1631. Path With Minimum Effort
# https://leetcode.com/problems/path-with-minimum-effort/

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        # BFS
        def canReachDestination(effort):
            visited = {(0, 0)}
            queue = collections.deque([(0, 0)])
            
            while queue:
                x, y = queue.popleft()
                if (x, y) == (m - 1, n - 1): return True
                
                for i, j in (x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1):
                    if m > i >= 0 <= j < n and (i, j) not in visited and abs(heights[i][j] - heights[x][y]) <= effort:
                        visited.add((i, j))
                        queue.append((i, j))
                    
            return False
        
        m, n = len(heights), len(heights[0])
        low, high = 0, 10 ** 6
        while low < high:
            effort = (low + high) >> 1
            if canReachDestination(effort):
                high = effort
            else:
                low = effort + 1
        return low
        