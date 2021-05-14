# 450. Delete Node in a BST

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root == None:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left == None:
                # also handles the case when leaf node is to be deleted
                return root.right
            elif root.right == None:
                return root.left
            else:
                in_suc = self.getInorderSuccessor(root)
                root.val = in_suc.val
                root.right = self.deleteNode(root.right, in_suc.val)
            
        return root
    
    def getInorderSuccessor(self, root: TreeNode) -> TreeNode:
        cur = root.right
        
        while cur and cur.left:
            cur = cur.left
        
        return cur
    