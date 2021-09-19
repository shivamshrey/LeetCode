# 210. Course Schedule II

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)] # adjacency list
        visited = [False] * numCourses
        in_degrees = [0] * numCourses
        
        for dest, src in prerequisites:
            graph[src].append(dest)
            in_degrees[dest] += 1
            
        queue = collections.deque([u for u in range(numCourses) if in_degrees[u] == 0])
        
        result = []
        while queue:
            u = queue.popleft()
            result.append(u)
            
            for v in graph[u]:
                in_degrees[v] -= 1
                if in_degrees[v] == 0:
                    queue.append(v)
        
        return result if len(result) == numCourses else []
    