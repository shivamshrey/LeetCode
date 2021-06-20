# 563. Binary Tree Tilt

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        def valueSum(root):
            if root == None:
                return 0
            left_sum = valueSum(root.left)
            right_sum = valueSum(root.right)
            self.result += abs(left_sum - right_sum)
            return left_sum + right_sum + root.val
        
        self.result = 0
        valueSum(root)
        return self.result
    