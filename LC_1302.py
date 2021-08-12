# 1302. Deepest Leaves Sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = collections.deque()
        if root:
            queue.append(root)
        
        result = 0
        
        while queue:
            size = len(queue)
            result = 0  # reset result = 0 before every level
            for _ in range(size):
                node = queue.popleft()
                result += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return result
    