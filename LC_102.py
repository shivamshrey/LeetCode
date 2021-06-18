# 102. Binary Tree Level Order Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = deque()
        if root:
            queue.append(root)
        result = []
        
        while queue:
            size = len(queue)
            cur_level = []
            for i in range(size):
                node = queue.popleft()
                cur_level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(cur_level)
        
        return result
    