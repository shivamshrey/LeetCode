# 1261. Find Elements in a Contaminated Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    # TC: O(n)
    # SC: O(n)
    def __init__(self, root: Optional[TreeNode]):
        def dfs(root, val):
            if root:
                root.val = val
                self.seen.add(val)
                dfs(root.left, 2 * val + 1)
                dfs(root.right, 2 * val + 2)
        
        self.seen = set()
        dfs(root, 0)

    # TC: O(1)
    # SC: O(1)
    def find(self, target: int) -> bool:
        return target in self.seen


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)