# 207. Course Schedule

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        in_degrees = [0] * numCourses
        
        for u, v in prerequisites:
            graph[v].append(u)
            in_degrees[u] += 1
            
        queue = collections.deque()
        
        for u in range(len(in_degrees)):
            if in_degrees[u] == 0:
                queue.append(u)
        
        count = 0
        while queue:
            u = queue.popleft()
            count += 1
            for v in graph[u]:
                in_degrees[v] -= 1
                if in_degrees[v] == 0:
                    queue.append(v)
        
        return count == numCourses
        