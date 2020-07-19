/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public int[] nextLargerNodes(ListNode head) {
        ArrayList<Integer> nodeVals = new ArrayList<>();
        ListNode cur = head;
        
        while (cur != null) {
            nodeVals.add(cur.val);
            cur = cur.next;
        }
        
        int[] result = new int[nodeVals.size()];
        Stack<Integer> stack = new Stack<>();
        
        for (int i = 0; i < nodeVals.size(); i++) {
            while (!stack.empty() && nodeVals.get(stack.peek()) < nodeVals.get(i))
                result[stack.pop()] = nodeVals.get(i);
            
            stack.push(i);
        }
        
        return result;
    }
}
