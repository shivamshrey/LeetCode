# 1293. Shortest Path in a Grid with Obstacles Elimination
# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/

# Time Complexity: O(N⋅K)
# Space Complexity: O(N⋅K)
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        target = (rows - 1, cols - 1)
        
        # if sufficient quota to eliminate obstacles is available,
        # then shortest path is Manhattan distance
        if k >= (rows - 1) + (cols - 1):
            return (rows - 1) + (cols - 1)
            
        # (row, col, remaining quota k)
        state = (0, 0, k)
        # (steps, state)
        queue = collections.deque([(0, state)])
        seen = set([state])
        
        while queue:
            steps, (row, col, k) = queue.popleft()
            
            if (row, col) == target:
                return steps
            
            for i, j in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                new_row, new_col = row + i, col + j
                
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    new_k = k - grid[new_row][new_col]
                    new_state = (new_row, new_col, new_k)
                    
                    if new_k >= 0 and new_state not in seen:
                        seen.add(new_state)
                        queue.append((steps + 1, new_state))
                        
        return -1
