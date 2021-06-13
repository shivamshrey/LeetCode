# 199. Binary Tree Right Side View

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root == None:
            return
        result = []
        queue = deque()
        queue.append(root)
        
        while queue:
            size = len(queue)
            for i in range(size):
                cur = queue.popleft()
                if i == size - 1:
                    result.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        
        return result
    