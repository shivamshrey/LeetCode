# 113. Path Sum II

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        def dfs(root, total, path, result):
            if root:
                if not root.left and not root.right and total == root.val:
                    path.append(root.val)
                    result.append(path)
                else:
                    dfs(root.left, total - root.val, path + [root.val], result)
                    dfs(root.right, total - root.val, path + [root.val], result)
            
            
        result = []
        dfs(root, targetSum, [], result)
        
        return result    
