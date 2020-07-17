/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    List<Integer> result = new ArrayList<>();
    
    public List<Integer> inorderTraversal(TreeNode root) {
        
        if (root != null)
            helper(root);
        
        return result;
    }
    
    public void helper(TreeNode root) {
        if (root.left != null)
            helper(root.left);
        
        result.add(root.val);
        
        if (root.right != null)
            helper(root.right);
    }
}
