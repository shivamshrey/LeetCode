# 106. Construct Binary Tree from Inorder and Postorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
    
        def buildTreeUtil(inorder_start, inorder_end):
            nonlocal postorder_index

            if inorder_start > inorder_end:
                return None

            root = TreeNode(postorder[postorder_index])
            postorder_index -= 1

            root.right = buildTreeUtil(hm[root.val] + 1, inorder_end)
            root.left = buildTreeUtil(inorder_start, hm[root.val] - 1)

            return root
        
        # build a hashmap to store value -> its index relations
        hm = dict()
        for i, value in enumerate(inorder):
            hm[value] = i
            
        postorder_index = len(postorder) - 1

        return buildTreeUtil(0, len(inorder) - 1)
        