# 1008. Construct Binary Search Tree from Preorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def buildBST(inorder_start, inorder_end):
            nonlocal preorder_index
            if inorder_start > inorder_end:
                return None
            
            root = TreeNode(preorder[preorder_index])
            preorder_index += 1
            
            root.left = buildBST(inorder_start, hashmap[root.val] - 1)
            root.right = buildBST(hashmap[root.val] + 1, inorder_end)
            
            return root
        
        inorder = sorted(preorder)
        hashmap = dict()
        for index, value in enumerate(inorder):
            hashmap[value] = index
        
        preorder_index = 0
        return buildBST(0, len(inorder) - 1)
    