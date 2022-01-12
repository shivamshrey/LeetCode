# 1022. Sum of Root To Leaf Binary Numbers

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(root, cur_num):
            nonlocal result
            if root:
                cur_num = (cur_num << 1) | root.val
                # if it's a leaf, update result
                if not root.left and not root.right:
                    result += cur_num
            
                dfs(root.left, cur_num)
                dfs(root.right, cur_num)
            
        result = 0
        dfs(root, 0)
        return result
        