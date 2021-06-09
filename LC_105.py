# 105. Construct Binary Tree from Preorder and Inorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        def buildTreeUtil(inorder_start, inorder_end):
            nonlocal preorder_index
            
            if inorder_start > inorder_end:
                return None
            
            root = TreeNode(preorder[preorder_index])
            preorder_index += 1
            
            root.left = buildTreeUtil(inorder_start, hm[root.val] - 1)
            root.right = buildTreeUtil(hm[root.val] + 1, inorder_end)
            
            return root
        
        # build a hashmap to store value -> its index relations
        hm = dict()
        for i, value in enumerate(inorder):
            hm[value] = i
            
        preorder_index = 0
        
        return buildTreeUtil(0, len(inorder) - 1)
    