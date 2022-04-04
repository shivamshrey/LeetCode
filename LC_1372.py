# 1372. Longest ZigZag Path in a Binary Tree
# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/

# TC: O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def maxZigZag(root, direction_to_go):
            nonlocal max_steps
            if not root: return -1
            
            left = maxZigZag(root.left, "right")
            right = maxZigZag(root.right, "left")
            
            max_steps = max(max_steps, max(left, right) + 1)
            
            return left + 1 if direction_to_go == 'left' else right + 1
        
        max_steps = 0
        maxZigZag(root, 'left') # could be 'right' as well
        return max_steps
                    