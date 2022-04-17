# 399. Evaluate Division
# https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def backtrack(source, target, product, visited):
            visited.add(source)
            return_val = -1.0
            
            neighbors = graph[source]
            if target in neighbors:
                return_val = product * neighbors[target]
            else:
                for neighbor, value in neighbors.items():
                    if neighbor not in visited:
                        return_val = backtrack(neighbor, target, product * value, visited)
                    
                    if return_val != -1.0:
                        break
            visited.remove(source)
            return return_val
        
        graph = collections.defaultdict(collections.defaultdict)
        
        for (dividend, divisor), value in zip(equations, values):
            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1 / value
            
        result = []
        for dividend, divisor in queries:
            if dividend not in graph or divisor not in graph:
                return_val = -1.0
            elif dividend == divisor:
                return_val = 1.0
            else:
                visited = set()
                return_val = backtrack(dividend, divisor, 1, visited)
            
            result.append(return_val)
            
        return result
        