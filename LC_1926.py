# 1926. Nearest Exit from Entrance in Maze
# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        queue = collections.deque([[entrance[0], entrance[1], 0]])
        while queue:
            i, j, distance = queue.popleft()
            
            if ([i, j] != entrance
                and (i in (0, m - 1) 
                     or j in (0, n - 1))):
                return distance
            
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if (0 <= i + di < m and 0 <= j + dj < n 
                    and maze[i + di][j + dj] != '+'):
                    queue.append([i + di, j + dj, distance + 1])
                    maze[i + di][j + dj] = '+' # mark as visited
        
        return -1
    