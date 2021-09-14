# 547. Number of Provinces

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [False] * len(isConnected)
        count = 0
        
        for i in range(len(isConnected)):
            if not visited[i]:
                self.dfs(i, isConnected, visited)
                count += 1
        return count
    
    def dfs(self, i, isConnected, visited):
        visited[i] = True
        for j in range(len(isConnected[i])):
            if not visited[j] and i != j and isConnected[i][j] == 1:
                self.dfs(j, isConnected, visited)
    