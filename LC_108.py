# 108. Convert Sorted Array to Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.buildBST(nums, 0, len(nums) - 1)
    
    def buildBST(self, nums, low, high):
        if low <= high:
            mid = low + (high - low) // 2
            root = TreeNode(nums[mid])
            root.left = self.buildBST(nums, low, mid - 1)
            root.right = self.buildBST(nums, mid + 1, high)
            return root
        return None
        