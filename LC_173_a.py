# 173. Binary Search Tree Iterator

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        def inorderTraversal(root):
            if root:
                inorderTraversal(root.left)
                self.inorder.append(root.val)
                inorderTraversal(root.right)
        self.inorder = []
        inorderTraversal(root)
        self.itr = -1

    def next(self) -> int:
        self.itr += 1
        return self.inorder[self.itr]

    def hasNext(self) -> bool:
        return self.itr + 1 < len(self.inorder)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
