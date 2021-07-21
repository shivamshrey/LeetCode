# 1823. Find the Winner of the Circular Game

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        queue = collections.deque([i for i in range(1, n + 1)])
        
        while len(queue) > 1:
            queue.rotate(-(k - 1))
            queue.popleft()
        
        return queue[0]
    