# 752. Open the Lock

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        depth = -1
        visited = set(deadends)
        queue = deque(["0000"])
        
        while queue:
            depth += 1
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if node == target:
                    return depth
                if node in visited:
                    continue
                
                visited.add(node)
                queue.extend(self.successors(node))
        
        return -1
        
    
    def successors(self, source):
        result = []
        for i, ch in enumerate(source):
            num = int(ch)
            result.append(source[:i] + str((num - 1) % 10) + source[i + 1:])
            result.append(source[:i] + str((num + 1) % 10) + source[i + 1:])
        
        return result
    