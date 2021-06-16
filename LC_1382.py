# 1382. Balance a Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.arr = []
        self.inorder(root)
        return self.buildBSTFromSortedArray(0, len(self.arr) - 1)
        
    def inorder(self, root):
        if root == None:
            return None
        self.inorder(root.left)
        self.arr.append(root.val)
        self.inorder(root.right)
    
    def buildBSTFromSortedArray(self, start, end):
        if start <= end:
            mid = start + (end - start) // 2
            root = TreeNode(self.arr[mid])
            root.left = self.buildBSTFromSortedArray(start, mid - 1)
            root.right = self.buildBSTFromSortedArray(mid + 1, end)
            return root
            