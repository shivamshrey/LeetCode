# 429. N-ary Tree Level Order Traversal

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        result = []
        queue = collections.deque()
        if root:
            queue.append(root)
        
        while queue:
            temp = []
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                temp.append(node.val)
            
                for child in node.children:
                    queue.append(child)
            
            result.append(temp)
        
        return result
    